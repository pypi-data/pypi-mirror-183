import django_tables2 as tables

from utilities.tables import BaseTable, ToggleColumn

from .models.LVMModel import LVMModel


class LVMModelTable(BaseTable):
    """Table for displaying LVMModel information"""

    pk = ToggleColumn()
    device_type = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = LVMModel
        fields = (
            "pk",
            "volume_group",
            "logical_volume",
            "size",
            "path"
        )


class LVMModelBulkTable(BaseTable):
    device_type = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = LVMModel
        fields = (
            "pk",
            "volume_group",
            "logical_volume",
            "size",
            "path"
        )
