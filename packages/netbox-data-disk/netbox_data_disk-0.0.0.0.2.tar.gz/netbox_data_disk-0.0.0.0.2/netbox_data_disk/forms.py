from django import forms
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from dcim.models import Device, Interface, Location, Rack, Region, Site, SiteGroup
from ipam.choices import *
from ipam.constants import *
from ipam.formfields import IPNetworkFormField
from ipam.models import *
from .models.disk import *
from netbox.forms import NetBoxModelForm
from tenancy.forms import TenancyForm
from utilities.exceptions import PermissionsViolation
from utilities.forms import (
    add_blank_choice, BootstrapMixin, CommentField, ContentTypeChoiceField, DatePicker, DynamicModelChoiceField,
    DynamicModelMultipleChoiceField, NumericArrayField, SlugField, StaticSelect, StaticSelectMultiple,
)
from virtualization.models import Cluster, ClusterGroup, VirtualMachine, VMInterface

__all__ = (
    'DataDiskForm'
)


class DataDiskForm(NetBoxModelForm):
    virtual_machine = DynamicModelChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False
    )

    class Meta:
        model = DataDisk
        fields = [
            'virtual_machine', 'size', 'vg_name', 'lv_name', 'mount_path'
        ]
