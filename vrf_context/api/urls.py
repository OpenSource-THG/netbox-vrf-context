from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'vrf_context'

router = NetBoxRouter()
router.register('vrf_contexts', views.VRFContextViewSet)

urlpatterns = router.urls
