from netbox.views import generic

from netbox_data_disk.models import View, Zone
from netbox_data_disk.filters import ViewFilter, ZoneFilter
from netbox_data_disk.forms import ViewForm, ViewFilterForm, ViewImportForm, ViewBulkEditForm
from netbox_data_disk.tables import ViewTable, ZoneTable

from utilities.views import ViewTab, register_model_view


class ViewView(generic.ObjectView):
    queryset = View.objects.all().prefetch_related("zone_set")


class ViewListView(generic.ObjectListView):
    queryset = View.objects.all()
    table = ViewTable
    filterset = ViewFilter
    filterset_form = ViewFilterForm


class ViewEditView(generic.ObjectEditView):
    queryset = View.objects.all()
    form = ViewForm
    default_return_url = "plugins:netbox_data_disk:view_list"


class ViewDeleteView(generic.ObjectDeleteView):
    queryset = View.objects.all()
    default_return_url = "plugins:netbox_data_disk:view_list"


class ViewBulkImportView(generic.BulkImportView):
    queryset = View.objects.all()
    model_form = ViewImportForm
    table = ViewTable
    default_return_url = "plugins:netbox_data_disk:view_list"


class ViewBulkEditView(generic.BulkEditView):
    queryset = View.objects.all()
    filterset = ViewFilter
    table = ViewTable
    form = ViewBulkEditForm


class ViewBulkDeleteView(generic.BulkDeleteView):
    queryset = View.objects.all()
    table = ViewTable


@register_model_view(View, "zones")
class ViewZoneListView(generic.ObjectChildrenView):
    queryset = View.objects.all().prefetch_related("zone_set")
    child_model = Zone
    table = ZoneTable
    filterset = ZoneFilter
    template_name = "netbox_data_disk/zone/child.html"
    hide_if_empty = True

    tab = ViewTab(
        label="Zones",
        permission="netbox_data_disk.view_zone",
        badge=lambda obj: obj.zone_set.count(),
        hide_if_empty=True,
    )

    def get_children(self, request, parent):
        return parent.zone_set
