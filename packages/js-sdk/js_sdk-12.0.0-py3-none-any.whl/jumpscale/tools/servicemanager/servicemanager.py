"""
### Description

Service manager is the service that monitors and manages background services through gevent greenlets.
Each service defines an interval to define the period of the service and defines also a job method that is run each period.
Any service should:
- Inherit from `BackgroundService` class defined here: `from jumpscale.tools.servicemanager.servicemanager import BackgroundService`
- Define an interval in the constructor
- Implement the abstract `job` method of the `BackgroundService` base class.

### How it schedules services

The service manager uses gevent greenlets to run jobs. It spawns the job in a greenlet after its interval period.
Rescheduling the service job is done in by linking a callback to the greenlet which is run after the greenlet finishes.
After the greenlet finishes execution the callback is fired which schedules the job to be run again after another interval.

To add a service to the service manager you should call the `add_service` method which takes the package name and package path as parameters.
It loads the file in this path as a module and gets the service object defined in the service.py file.

### Immediately schedule service

The services first start will be after the requested interval.
If you need to make the service first interval immediately on server start, It can be added in your service by adding

```python3
self.schedule_on_start = True
```

in your service init after calling super() init.


### Example service

```python3
from jumpscale.tools.servicemanager.servicemanager import BackgroundService

class TestService(BackgroundService):
    def __init__(self, interval="* * * * *", *args, **kwargs):
        '''
            Test service that runs every 1 minute
        '''
        super().__init__(interval, *args, **kwargs)
        self.schedule_on_start = True # immediately schedule the service (optional step and the line can be removed, default=False)

    def job(self):
        print("[Test Service] Done")

service = TestService()
```
"""

from numbers import Real
from math import ceil
from abc import ABC, abstractmethod
from signal import SIGTERM, SIGKILL
from crontab import CronTab
import gevent
from gevent.pool import Pool

from jumpscale.loader import j
from jumpscale.core.base import Base
from multiprocessing import cpu_count


class BackgroundService(ABC):
    def __init__(self, interval=60, *args, **kwargs):
        """Abstract base class for background services managed by the service manager

        Arguments:
            interval (int | CronTab object | str): scheduled job is executed every interval in seconds / CronTab object / CronTab-formatted string
        """
        self.interval = interval
        self.schedule_on_start = False

    @abstractmethod
    def job(self):
        """
        Background job to be scheduled.
        Should be implemented by any service that inherits from this class
        """
        pass


# TODO: add support for non-periodic tasks
# TODO: configurable services
# TODO: add support for services not in packages
class ServiceManager(Base):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.services = {}  # service objects
        self._scheduled = {}  # greenlets of scheduled services
        self._running = {}  # greenlets of currently running services
        self._pool = Pool(cpu_count())

    @staticmethod
    def seconds_to_next_interval(interval):
        """Helper method to get seconds remaining to next_interval

        Arguments:
            interval (Any): next interval to which seconds remaining is calculated

        Returns:
            Real: number of seconds remaining until next interval

        Raises:
            ValueError: when the type of interval is not Real / CronTab object / CronTab string format
        """
        if isinstance(interval, Real):
            return interval
        elif isinstance(interval, str):
            try:
                return CronTab(interval).next(default_utc=True)
            except Exception as e:
                raise j.exceptions.Value(str(e))
        elif isinstance(interval, CronTab):
            return interval.next(default_utc=True)
        else:
            raise j.exceptions.Runtime(f"Unsupported interval type: {type(interval)}")

    @staticmethod
    def _load_service(path):
        """Load the module in the service file path and get the service object

        Arguments:
            path (str): path of the service file

        Returns:
            service: service object defined in the service file
        """
        module = j.tools.codeloader.load_python_module(path, force_reload=True)
        return module.service

    @staticmethod
    def __on_exception(greenlet):
        """Callback to handle exception raised by service greenlet

        Arguments:
            greenlet (Greenlet): greenlet object
        """
        message = f"Service {greenlet.service.name} raised an exception: {greenlet.exception}"
        j.tools.alerthandler.alert_raise(app_name="servicemanager", message=message, alert_type="exception")
        j.logger.exception(f"Service {greenlet.service.name} raised an exception", exception=greenlet.exception)

    def __callback(self, greenlet):
        """Callback runs after greenlet finishes execution

        Arguments:
            greenlet (Greenlet): greenlet object
        """
        greenlet.unlink(self.__callback)
        if greenlet.service.name in self._running:
            self._running.pop(greenlet.service.name)

    def _schedule_service(self, service):
        """Runs a service job and schedules it to run again every period (interval) specified by the service

        Arguments:
            service (BackgroundService): background service object
        """
        if service.name not in self._running:
            greenlet = self._pool.apply_async(service.job)
            greenlet.link(self.__callback)
            greenlet.link_exception(self.__on_exception)
            greenlet.start()
            self._running[service.name] = greenlet
            self._running[service.name].service = service
        next_start = ceil(self.seconds_to_next_interval(service.interval))
        self._scheduled[service.name] = gevent.spawn_later(next_start, self._schedule_service, service=service)

    def start(self):
        """Start the service manager and schedule default services"""
        # schedule default services
        for service in self.services.values():
            next_start = ceil(self.seconds_to_next_interval(service.interval))
            self._scheduled[service.name] = gevent.spawn_later(next_start, self._schedule_service, service=service)

    def stop(self):
        """Stop all background services"""
        j.logger.info("Stopping background services")
        for service in list(self.services.keys()):
            self.stop_service(service)
        j.logger.info("Done stopping the background services")

    def add_service(self, service_name, service_path):
        """Add a new background service to be managed and scheduled by the service manager

        Arguments:
            service_path (str): absolute path of the service file
        """

        service = self._load_service(service_path)
        service.name = service_name

        if service in self.services.values():
            j.logger.debug(f"Service {service.name} is already running. Reloading...")
            self.stop_service(service.name)

        next_start = 0 if service.schedule_on_start else ceil(self.seconds_to_next_interval(service.interval))
        self._scheduled[service.name] = gevent.spawn_later(next_start, self._schedule_service, service=service)
        self.services[service.name] = service
        j.logger.debug(f"Service {service.name} is added.")

    def stop_service(self, service_name, block=True):
        """Stop a running background service and unschedule it if it's scheduled to run again

        Arguments:
            service_name (str): name of the service to be stopped
            block (bool): wait for service job to finish. if False, service job will be killed without waiting
        """
        if service_name not in self.services:
            raise j.exceptions.Value(f"Service {service_name} is not running")

        # unschedule service if it's scheduled to run again
        if service_name in self._scheduled:
            greenlet = self._scheduled[service_name]
            greenlet.unlink(self.__callback)
            greenlet.kill()
            if not greenlet.dead:
                raise j.exceptions.Runtime("Failed to unschedule greenlet")
            self._scheduled.pop(service_name)

        # wait for service to finish if it's already running
        if service_name in self._running:
            greenlet = self._running[service_name]
            greenlet.unlink(self.__callback)
            if block:
                try:
                    j.logger.info(f"Waiting the service {service_name} to finish")
                    greenlet.join()
                    j.logger.info(f"Done waiting the service {service_name}")
                except Exception as e:
                    raise j.exceptions.Runtime(f"Exception on waiting for greenlet: {str(e)}")
            else:
                try:
                    greenlet.kill()
                except Exception as e:
                    raise j.exceptions.Runtime(f"Exception on killing greenlet: {str(e)}")
                if not greenlet.dead:
                    raise j.exceptions.Runtime("Failed to kill running greenlet")

        self.services.pop(service_name)
