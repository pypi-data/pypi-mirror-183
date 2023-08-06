from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        from netbox_data_disk.models import Backup, BackupJob

        for backup in Backup.objects.all():
            if BackupJob.needs_enqueue(backup=backup):
                BackupJob.enqueue_if_needed(backup=backup)
                print(f'Backup: {backup} has been queued')

