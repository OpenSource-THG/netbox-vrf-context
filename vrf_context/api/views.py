from django.db.models import Count

from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import VRFContextSerializer


class VRFContextViewSet(NetBoxModelViewSet):
    queryset = models.VRFContext.objects.prefetch_related('tags')
    serializer_class = VRFContextSerializer

