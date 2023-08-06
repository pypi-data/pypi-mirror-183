from django.urls import reverse
from django.test import SimpleTestCase

from netbox_test_plugin import __version__
from netbox_test_plugin.tests.custom import APITestCase


class NetboxTestPluginVersionTestCase(SimpleTestCase):
    """
    Test for netbox_test_plugin package
    """

    def test_version(self):
        assert __version__ == "0.16.1"


class AppTest(APITestCase):
    """
    Test the availability of the NetBox DNS API root
    """

    def test_root(self):
        url = reverse("plugins-api:netbox_test_plugin-api:api-root")
        response = self.client.get(f"{url}?format=api", **self.header)

        self.assertEqual(response.status_code, 200)
