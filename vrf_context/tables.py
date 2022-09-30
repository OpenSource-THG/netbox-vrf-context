import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import VRFContext

class VRFContextTable(NetBoxTable):

    vrf = tables.Column(
        linkify=True
    )
    device = tables.Column(
        linkify=True
    )


    class Meta(NetBoxTable.Meta):
        model = VRFContext
        fields = ('pk', 'id', 'vrf', 'device')
        default_columns = ('id', 'vrf', 'device')
