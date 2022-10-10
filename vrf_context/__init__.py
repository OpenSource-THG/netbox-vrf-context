from extras.plugins import PluginConfig


class VRFContext(PluginConfig):
    name = "vrf_context"
    verbose_name = "VRF Context"
    description = "VRF Context in Netbox"
    version = "0.1"
    author = "The Hut Group"
    author_email = "info@thehutgroup.com"
    base_url = "vrf-context"
    required_settings = []
    default_settings = {}


config = VRFContext
