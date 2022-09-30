from netbox.filtersets import NetBoxModelFilterSet
from .models import VRFContext


class AccessListRuleFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = VRFContext
        fields = ('id', 'vrf', 'device', 'comments')

    #def search(self, queryset, name, value):
    #    return queryset.filter(description__icontains=value)
