"""
Map Views to URLs.
"""

from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views

urlpatterns = (
    # Access Lists
    path("data-disk/", views.DataDiskListView.as_view(), name="datadisk_list"),
    path(
        "data-disk/add/",
        views.DataDiskEditView.as_view(),
        name="datadisk_add",
    ),
    # path('access-lists/edit/', views.AccessListBulkEditView.as_view(), name='accesslist_bulk_edit'),
    path('data-disk/<int:pk>/', views.DataDiskListView.as_view(), name='datadisk'),
    path('data-disk/<int:pk>/edit/', views.DataDiskListView.as_view(), name='datadisk_edit'),
    path('data-disk/<int:pk>/delete/', views.DataDiskListView.as_view(), name='datadisk_delete'),
)
