from django.urls import path

from .views import (
    LVMModelBulkDeleteView,
    LVMModelCreateView,
    LVMModelImportView,
    LVMModelListView,
)

urlpatterns = [
    path("lvmmodel/", LVMModelListView.as_view(), name="lvmmodel_list"),
    path("lvmmodel/add/", LVMModelCreateView.as_view(), name="lvmmodel_add"),
    path("lvmmodel/import/", LVMModelImportView.as_view(), name="lvmmodel_import"),
    path("lvmmodel/delete/", LVMModelBulkDeleteView.as_view(), name="lvmmodel_bulk_delete"),
]
