from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name="DataDisk",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ("size", models.CharField(blank=True, max_length=255, null=True)),
                ("vg_name", models.CharField(max_length=255)),
                ("lv_name", models.CharField(max_length=255)),
                ("mount_path", models.CharField(max_length=255)),
                (
                    "virtual_machine",
                    models.OneToOneField(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="virtualization.VirtualMachine"
                    ),
                ),
            ],
        ),
    ]