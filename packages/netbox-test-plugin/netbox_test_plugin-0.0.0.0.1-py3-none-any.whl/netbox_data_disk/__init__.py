from extras.plugins import PluginConfig

__version__ = "0.0.0.0.1"


class TestPluginConfig(PluginConfig):
    name = "netbox_test_plugin"
    verbose_name = "Netbox Test Plugin"
    description = "Netbox Test Plugin"
    min_version = "3.4.0"
    version = __version__
    author = "Aurora Research Lab"
    author_email = "info@aurorabilisim.com"
    required_settings = []
    default_settings = {
        "zone_default_ttl": 86400,
        "zone_soa_serial_auto": True,
        "zone_soa_serial": 1,
        "zone_soa_refresh": 172800,
        "zone_soa_retry": 7200,
        "zone_soa_expire": 2592000,
        "zone_soa_minimum": 3600,
        "feature_ipam_integration": False,
    }
    base_url = "netbox-test-plugin"


config = TestPluginConfig
