from rest_framework import serializers

from netbox.api import SerializedPKRelatedField
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from dcim.api.serializers import NestedDeviceSerializer
from ipam.api.serializers import NestedVRFSerializer
from netbox_bgp.models import BGPSession
from netbox_bgp.api.serializers import NestedBGPSessionSerializer
from netbox_static_routes.models import StaticRoute
from netbox_static_routes.api.serializers import NestedStaticRouteSerializer

from ..models import VRFContext

class VRFContextSerializer(NetBoxModelSerializer):
    device = NestedDeviceSerializer()
    vrf = NestedVRFSerializer()
    bgp_sessions = SerializedPKRelatedField(
        queryset=BGPSession.objects.all(),
        serializer=NestedBGPSessionSerializer,
        required=False,
        many=True
    )
    static_routes = SerializedPKRelatedField(
        queryset=StaticRoute.objects.all(),
        serializer=NestedStaticRouteSerializer,
        required=False,
        many=True
    )


    class Meta:
        model = VRFContext
        fields = (
            'id', 'vrf', 'device', 'comments', 'tags', 'bgp_sessions',
            'static_routes', 'custom_fields', 'created', 'last_updated',
        )

class NestedVRFContextSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:vrf_contexts-api:vrfcontext-detail'
    )

    class Meta:
        model = VRFContext
        fields = ('id', 'vrf', 'device', 'comments', 'tags', 'url')
