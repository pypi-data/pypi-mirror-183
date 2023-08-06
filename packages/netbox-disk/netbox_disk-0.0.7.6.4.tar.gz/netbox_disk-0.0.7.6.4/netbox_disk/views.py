
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from netbox.views.generic import BulkDeleteView, BulkImportView, ObjectEditView, ObjectListView

from .forms import PDUConfigCSVForm, PDUConfigFilterForm, PDUConfigForm
from .models.LVMModel import LVMModel
from .tables import LVMModelBulkTable, LVMModelTable

from django.conf import settings
from packaging import version

NETBOX_CURRENT_VERSION = version.parse(settings.VERSION)


class LVMModelListView(ObjectListView):
    """View for listing all LVMModel items"""

    queryset = LVMModel.objects.all()
    table = LVMModelTable
    template_name = "netbox_disk/lvmmodel_list.html"


class LVMModelCreateView(PermissionRequiredMixin, ObjectEditView):
    """View for creating a new LVMModel"""

    model = LVMModel
    queryset = LVMModel.objects.all()
    template_name = "netbox_disk/lvmmodel_edit.html"
    default_return_url = "plugins:netbox_disk:lvmmodel_list"


class LVMModelImportView(BulkImportView):
    """View for bulk-importing a CSV file to create PDUConfigs"""

    queryset = LVMModel.objects.all()
    table = LVMModelBulkTable
    default_return_url = "plugins:netbox_disk:lvmmodel_list"


class LVMModelBulkDeleteView(BulkDeleteView):
    """View for deleting one or more LVMModels."""

    queryset = LVMModel.objects.filter()
    table = LVMModelTable
    default_return_url = "plugins:netbox_disk:lvmmodel_list"
