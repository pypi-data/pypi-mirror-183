import re

from extras.plugins import PluginTemplateExtension  # pylint: disable=import-error

from . import livestatus
from .models.LVMModel import LVMModel


class DiskStatus(PluginTemplateExtension):
    def __init__(self, context):
        super().__init__(context)
        self.settings = self.context["settings"].PLUGINS_CONFIG["netbox_disk"]
        self.hostname = self.context["object"].name or ""  # name can be None.
        self.livestatus_host = self.get_livestatus_host()
        self.livestatus_port = self.settings["livestatus_port"]
        self.disk_base_url = self.get_disk_base_url()

    def get_livestatus_host(self):
        """Uses settings and potential overrides to determine the Disk host."""
        for regex, livestatus_host in self.settings["livestatus_host_overrides"]:
            if re.search(regex, self.hostname):
                return livestatus_host
        return self.settings["livestatus_host"]

    def get_disk_base_url(self):
        """Uses settings and potential overrides to determine the Disk url."""
        for regex, disk_base_url in self.settings["disk_base_url_overrides"]:
            if re.search(regex, self.hostname):
                return disk_base_url
        return self.settings["disk_base_url"]

    def buttons(self):
        """Adds an extra button at the top of the bage."""
        return self.render(
            "device_disk_buttons.html",
            extra_context={"disk_base_url": self.disk_base_url},
        )

    def left_page(self):
        """         extra_context["disk"] = livestatus.hoststatus(
                        self.hostname,
                        self.livestatus_host,
                        self.livestatus_port,
                    )
        """
        vg_name = ["docker"]
        lv_name = ["docker"]
        lvmmodel1 = LVMModel(volume_group="docker", logical_volume="docker", size="100", path="/var/lib/docker")
        lvmmodel2 = LVMModel(volume_group="data", logical_volume="data", size="100", path="/data")
        lvmmodel3 = LVMModel(volume_group="oracle", logical_volume="oracle", size="100", path="/oracle")
        lvm = [lvmmodel1, lvmmodel2, lvmmodel3]
        """Adds a status table to the page."""
        extra_context = {
            "disk_base_url": self.disk_base_url,
        }
        try:
            extra_context["disk"] = lvm
        except Exception:  # pylint: disable=broad-except
            # Be very defensive so that broken Disk doesn't break Netbox.
            pass
        return self.render("device_disk_box.html", extra_context=extra_context)


class DiskStatusDevice(DiskStatus):
    model = "dcim.device"


class DiskStatusVM(DiskStatus):
    model = "virtualization.virtualmachine"


template_extensions = [  # pylint: disable=invalid-name
    DiskStatusDevice,
    DiskStatusVM,
]
