from utilities.testing import APIViewTestCases

from netbox_test_plugin.tests.custom import APITestCase
from netbox_test_plugin.models import NameServer


class NameServerTest(
    APITestCase,
    APIViewTestCases.GetObjectViewTestCase,
    APIViewTestCases.ListObjectsViewTestCase,
    APIViewTestCases.CreateObjectViewTestCase,
    APIViewTestCases.UpdateObjectViewTestCase,
    APIViewTestCases.DeleteObjectViewTestCase,
):
    model = NameServer
    brief_fields = ["display", "id", "name", "url"]
    create_data = [
        {"name": "ns1.example.com"},
        {"name": "ns2.example.com"},
        {"name": "ns3.example.com"},
    ]

    @classmethod
    def setUpTestData(cls):
        nameservers = (
            NameServer(name="ns4.example.com"),
            NameServer(name="ns5.example.com"),
            NameServer(name="ns6.example.com"),
        )
        NameServer.objects.bulk_create(nameservers)
