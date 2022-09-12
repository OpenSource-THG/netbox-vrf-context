from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel

class VRFContext(NetBoxModel):
    vrf = models.ForeignKey(
        to='ipam.VRF',
        on_delete=models.CASCADE,
        related_name='contexts'
    )
    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.CASCADE,
        related_name='devices'
    )
    comments = models.TextField(
        blank=True
    )
    bgp_sessions = models.ManyToManyField('netbox_bgp.BGPSession')
    static_routes = models.ManyToManyField('netbox_static_routes.StaticRoute')

    def __str__(self):
        return f'{self.device}:{self.vrf}'

    def get_absolute_url(self):
        return reverse('plugins:vrf_context:vrfcontext', args=[self.pk])
