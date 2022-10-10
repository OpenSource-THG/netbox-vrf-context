from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (
    path('vrf-contexts/', views.VRFContextListView.as_view(), name='vrfcontext_list'),
    path('vrf-contexts/add/', views.VRFContextEditView.as_view(), name='vrfcontext_add'),
    path('vrf-contexts/<int:pk>/', views.VRFContextView.as_view(), name='vrfcontext'),
    path('vrf-contexts/<int:pk>/edit/', views.VRFContextEditView.as_view(), name='vrfcontext_edit'),
    path('vrf-contexts/<int:pk>/delete/', views.VRFContextDeleteView.as_view(), name='vrfcontext_delete'),
    path('access-lists/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='vrfcontext_changelog', kwargs={
        'model': models.VRFContext
    })
)
