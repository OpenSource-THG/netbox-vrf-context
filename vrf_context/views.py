from netbox.views import generic
from . import forms, models, tables

class VRFContextView(generic.ObjectView):
    queryset = models.VRFContext.objects.all()

class VRFContextListView(generic.ObjectListView):
    queryset = models.VRFContext.objects.all()
    table = tables.VRFContextTable

class VRFContextEditView(generic.ObjectEditView):
    queryset = models.VRFContext.objects.all()
    form = forms.VRFContextForm

class VRFContextDeleteView(generic.ObjectDeleteView):
    queryset = models.VRFContext.objects.all()
