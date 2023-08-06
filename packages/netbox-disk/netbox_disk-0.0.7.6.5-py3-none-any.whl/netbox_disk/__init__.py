try:
    from extras.plugins import PluginConfig
except ImportError:
    # Dummy so install of wheel works without Netbox.
    class PluginConfig:
        pass


from .version import VERSION


class NetboxDiskConfig(PluginConfig):
    """
    This class defines attributes for the NetBox Disk plugin.
    """

    # Plugin package name
    name = "netbox_disk"

    # Human-friendly name and description
    verbose_name = "Disk"
    description = "Plugin to show Disks in Netbox"

    # Plugin version
    version = VERSION

    # Plugin author
    author = "Tim Rhomberg"
    author_email = "timrhomberg@hotmail.com"

    # Configuration parameters that MUST be defined by the user (if any)
    # required_settings = ["livestatus_host", "disk_base_url"]

    # Default configuration parameter values, if not set by the user
    default_settings = {
        "livestatus_host_overrides": [],
        "livestatus_host": "example.org",
        "livestatus_port": 6557,
        "disk_base_url": "example.org",
        "disk_base_url_overrides": []
    }

    # Base URL path. If not set, the plugin name will be used.
    base_url = "disk"

    # Caching config
    caching_config = {}


config = NetboxDiskConfig  # pylint: disable=invalid-name
