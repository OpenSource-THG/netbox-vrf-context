from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse('plugins:vrf_context:vrfcontext', args=[self.pk])
    
