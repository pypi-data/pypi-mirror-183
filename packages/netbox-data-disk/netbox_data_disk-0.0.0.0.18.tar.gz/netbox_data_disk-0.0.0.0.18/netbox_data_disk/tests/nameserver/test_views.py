from utilities.testing import ViewTestCases
from utilities.testing import create_tags

from netbox_data_disk.tests.custom import ModelViewTestCase
from netbox_data_disk.models import NameServer


class NameServerTestCase(
    ModelViewTestCase,
    ViewTestCases.GetObjectViewTestCase,
    ViewTestCases.CreateObjectViewTestCase,
    ViewTestCases.EditObjectViewTestCase,
    ViewTestCases.DeleteObjectViewTestCase,
    ViewTestCases.ListObjectsViewTestCase,
    ViewTestCases.GetObjectChangelogViewTestCase,
    ViewTestCases.BulkImportObjectsViewTestCase,
    ViewTestCases.BulkDeleteObjectsViewTestCase,
):
    model = NameServer

    @classmethod
    def setUpTestData(cls):

        cls.nameservers = (
            NameServer(name="ns1.example.com"),
            NameServer(name="ns2.example.com"),
            NameServer(name="ns3.example.com"),
        )
        NameServer.objects.bulk_create(cls.nameservers)

        tags = create_tags("Alpha", "Bravo", "Charlie")

        cls.form_data = {
            "name": "ns4.example.com",
            "tags": [t.pk for t in tags],
        }

        cls.csv_data = (
            "name",
            "ns5.example.com",
            "ns6.example.com",
            "ns7.example.com",
        )

        cls.csv_update_data = (
            "id,name,description",
            f"{cls.nameservers[0].pk},ns8.hindenburgring.com,test1",
            f"{cls.nameservers[1].pk},ns9.hindenburgring.com,test2",
            f"{cls.nameservers[2].pk},ns10.hindenburgring.com,test3",
        )

    maxDiff = None
