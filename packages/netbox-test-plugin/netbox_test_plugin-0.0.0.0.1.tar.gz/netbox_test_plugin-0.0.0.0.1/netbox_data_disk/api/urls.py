from netbox.api.routers import NetBoxRouter

from netbox_test_plugin.api.views import (
    NetboxTestPluginRootView,
    ViewViewSet,
    ZoneViewSet,
    NameServerViewSet,
    RecordViewSet,
)

router = NetBoxRouter()
router.APIRootView = NetboxTestPluginRootView

router.register("views", ViewViewSet)
router.register("zones", ZoneViewSet)
router.register("nameservers", NameServerViewSet)
router.register("records", RecordViewSet)

urlpatterns = router.urls
