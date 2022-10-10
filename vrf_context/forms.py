from ipam.models import VRF
from dcim.models import Device
from netbox_bgp.models import BGPSession
from netbox_static_routes.models import StaticRoute
from netbox.forms import NetBoxModelForm
from utilities.forms.fields import \
    DynamicModelChoiceField, DynamicModelMultipleChoiceField
from .models import VRFContext

class VRFContextForm(NetBoxModelForm):
    vrf = DynamicModelChoiceField(
        queryset=VRF.objects.all()
    )
    device = DynamicModelChoiceField(
        queryset=Device.objects.all()
    )
    bgp_sessions = DynamicModelMultipleChoiceField(
        queryset=BGPSession.objects.all(),
        required=False
    )
    static_routes = DynamicModelMultipleChoiceField(
        queryset=StaticRoute.objects.all(),
        required=False,
        query_params = {
            'device': '$device'
        }
    )

    class Meta:
        model = VRFContext
        fields = ('vrf', 'device', 'comments', 'tags', 'bgp_sessions', 'static_routes')
