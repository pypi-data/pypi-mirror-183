from django import forms

from extras.forms import CustomFieldModelCSVForm
from utilities.forms import BootstrapMixin

from .models.LVMModel import LVMModel


class LVMModelForm(BootstrapMixin, forms.ModelForm):
    """Form for creating a new PDUConfig"""

    class Meta:
        model = LVMModel
        obj_type = "test"


class LVMModelFilterForm(BootstrapMixin, forms.ModelForm):
    """Form for siltering PDUConfig instances."""

    q = forms.CharField(required=False, label="Search")

    class Meta:
        model = LVMModel


class LVMModelCSVForm(CustomFieldModelCSVForm):
    """Form for entering CSV to bulk-import PDUConfig entries."""

    class Meta:
        model = LVMModel
        fields = LVMModel.csv_headers

    def save(self, commit=True, **kwargs):
        """Save the model"""
        model = super().save(commit=commit, **kwargs)
        return model
