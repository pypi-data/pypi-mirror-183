from netbox.api.routers import NetBoxRouter

from netbox_data_disk.api.views import (
    NetboxDataDiskRootView,
    ViewViewSet,
    ZoneViewSet,
    NameServerViewSet,
    RecordViewSet,
)

router = NetBoxRouter()
router.APIRootView = NetboxDataDiskRootView

router.register("views", ViewViewSet)
router.register("zones", ZoneViewSet)
router.register("nameservers", NameServerViewSet)
router.register("records", RecordViewSet)

urlpatterns = router.urls
