from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q
from django.db.models.functions import Lower
from django.urls import reverse

from dcim.models import BaseInterface
from extras.models import ConfigContextModel
from extras.querysets import ConfigContextModelQuerySet
from netbox.config import get_config
from netbox.models import NetBoxModel, PrimaryModel
from utilities.fields import NaturalOrderingField
from utilities.ordering import naturalize_interface
from utilities.query_functions import CollateAsChar
from virtualization.choices import *

__all__ = (
    'DataDisk',
)


class DataDisk(NetBoxModel):
    """
    A Service represents a layer-four service (e.g. HTTP or SSH) running on a Device or VirtualMachine. A Service may
    optionally be tied to one or more specific IPAddresses belonging to its parent.
    """
    virtual_machine = models.ForeignKey(
        to='virtualization.VirtualMachine',
        on_delete=models.CASCADE,
        related_name='disks',
        null=True,
        blank=True
    )
    size = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name='Disk (GB)'
    )
    vg_name = models.CharField(
        max_length=100
    )
    lv_name = models.CharField(
        max_length=100
    )
    mount_path = models.CharField(
        max_length=100
    )

    prerequisite_models = (
        'virtualization.VirtualMachine',
    )

    clone_fields = ['virtual_machine']

    class Meta:
        ordering = 'virtual_machine'  # (protocol, port) may be non-unique
        verbose_name = "Data Disk"
        verbose_name_plural = "Data Disk"

    def get_absolute_url(self):
        return reverse('plugins:netbox_data_disk:datadisk', args=[self.pk])

    @property
    def parent(self):
        return self.virtual_machine

    def clean(self):
        super().clean()

        # A Service must belong to a VirtualMachine
        if not self.device and not self.virtual_machine:
            raise ValidationError("A Disk must be associated with a virtual machine.")
