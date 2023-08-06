"""
Defines the business logic for the plugin.
Specifically, all the various interactions with a client.
"""

from netbox.views import generic

from netbox_data_disk import forms, tables
from archive.netbox_data_disk.models.disk import DataDisk

__all__ = (
    "DataDiskView",
    "DataDiskListView",
    "DataDiskEditView",
    "DataDiskDeleteView"
)


class DataDiskView(generic.ObjectListView):
    queryset = DataDisk.objects.all()


class DataDiskListView(generic.ObjectListView):
    queryset = DataDisk.objects.all()
    table = tables.DataDiskTable


class DataDiskEditView(generic.ObjectEditView):
    queryset = DataDisk.objects.all()
    form = forms.DataDiskForm


class DataDiskDeleteView(generic.ObjectDeleteView):
    queryset = DataDisk.objects.all()


# class ServiceCreateView(generic.ObjectEditView):
#     queryset = Service.objects.all()
#     form = forms.ServiceCreateForm
#     template_name = 'ipam/service_create.html'

