from netbox.views import generic

from netbox_test_plugin.filters import NameServerFilter, ZoneFilter
from netbox_test_plugin.forms import (
    NameServerImportForm,
    NameServerFilterForm,
    NameServerForm,
    NameServerBulkEditForm,
)
from netbox_test_plugin.models import Zone, NameServer
from netbox_test_plugin.tables import NameServerTable, ZoneTable

from utilities.views import ViewTab, register_model_view


class NameServerListView(generic.ObjectListView):
    queryset = NameServer.objects.all()
    filterset = NameServerFilter
    filterset_form = NameServerFilterForm
    table = NameServerTable


class NameServerView(generic.ObjectView):
    queryset = NameServer.objects.all().prefetch_related("zones")


class NameServerEditView(generic.ObjectEditView):
    queryset = NameServer.objects.all()
    form = NameServerForm
    default_return_url = "plugins:netbox_test_plugin:nameserver_list"


class NameServerDeleteView(generic.ObjectDeleteView):
    queryset = NameServer.objects.all()
    default_return_url = "plugins:netbox_test_plugin:nameserver_list"


class NameServerBulkImportView(generic.BulkImportView):
    queryset = NameServer.objects.all()
    model_form = NameServerImportForm
    table = NameServerTable
    default_return_url = "plugins:netbox_test_plugin:nameserver_list"


class NameServerBulkEditView(generic.BulkEditView):
    queryset = NameServer.objects.all()
    filterset = NameServerFilter
    table = NameServerTable
    form = NameServerBulkEditForm


class NameServerBulkDeleteView(generic.BulkDeleteView):
    queryset = NameServer.objects.all()
    table = NameServerTable


@register_model_view(NameServer, "zones")
class NameServerZoneListView(generic.ObjectChildrenView):
    queryset = NameServer.objects.all().prefetch_related("zones")
    child_model = Zone
    table = ZoneTable
    filterset = ZoneFilter
    template_name = "netbox_test_plugin/zone/child.html"
    hide_if_empty = True

    tab = ViewTab(
        label="Zones",
        permission="netbox_test_plugin.view_zone",
        badge=lambda obj: obj.zones.count(),
        hide_if_empty=True,
    )

    def get_children(self, request, parent):
        return parent.zones


@register_model_view(NameServer, "soa_zones")
class NameServerSOAZoneListView(generic.ObjectChildrenView):
    queryset = NameServer.objects.all().prefetch_related("zones_soa")
    child_model = Zone
    table = ZoneTable
    filterset = ZoneFilter
    template_name = "netbox_test_plugin/zone/child.html"
    hide_if_empty = True

    tab = ViewTab(
        label="SOA Zones",
        permission="netbox_test_plugin.view_zone",
        badge=lambda obj: obj.zones_soa.count(),
        hide_if_empty=True,
    )

    def get_children(self, request, parent):
        return parent.zones_soa
