from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from dcim.api.serializers import NestedDeviceSerializer
from ipam.api.serializers import NestedVRFSerializer

from ..models import VRFContext

class VRFContextSerializer(NetBoxModelSerializer):
    device = NestedDeviceSerializer()
    vrf = NestedVRFSerializer()

    class Meta:
        model = VRFContext
        fields = (
            'id', 'vrf', 'device', 'comments', 'tags', 'custom_fields', 'created',
            'last_updated',
        )

class NestedVRFContextSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:vrf_contexts-api:vrfcontext-detail'
    )

    class Meta:
        model = VRFContext
        fields = ('id', 'vrf', 'device', 'comments', 'tags', 'url')