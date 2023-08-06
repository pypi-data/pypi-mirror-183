import logging

from extras.plugins import PluginTemplateExtension

from netbox_data_disk.models import Backup, BackupJob
from netbox_data_disk.utils.backups import get_backup_tables

logger = logging.getLogger(f"netbox_data_disk")


class DeviceBackups(PluginTemplateExtension):
    model = 'dcim.device'

    def full_width_page(self):
        device = self.context.get('object', None)
        devices = Backup.objects.filter(device=device) if device is not None else Backup.objects.none()
        if devices.count() > 0:
            instance = devices.first()
            tables = get_backup_tables(instance)

            if BackupJob.is_queued(instance) is False:
                logger.debug(f'{instance}: Queuing Job')
                BackupJob.enqueue(instance)

            return self.render('netbox_data_disk/inc/backup_tables.html', extra_context={
                'running': tables.get('running'),
                'startup': tables.get('startup'),
            })

        return ''


template_extensions = [DeviceBackups]
