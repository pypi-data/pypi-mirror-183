def export_module_as():
    from jumpscale.core.base import StoredFactory
    from .backupjob import BackupJob

    return StoredFactory(BackupJob)
