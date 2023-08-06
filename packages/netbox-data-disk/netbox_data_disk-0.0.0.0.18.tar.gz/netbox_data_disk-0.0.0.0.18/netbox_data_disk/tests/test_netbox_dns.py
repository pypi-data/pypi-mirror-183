from django.urls import reverse
from django.test import SimpleTestCase

from netbox_data_disk import __version__
from netbox_data_disk.tests.custom import APITestCase


class NetboxDataDiskVersionTestCase(SimpleTestCase):
    """
    Test for netbox_data_disk package
    """

    def test_version(self):
        assert __version__ == "0.16.1"


class AppTest(APITestCase):
    """
    Test the availability of the NetBox DNS API root
    """

    def test_root(self):
        url = reverse("plugins-api:netbox_data_disk-api:api-root")
        response = self.client.get(f"{url}?format=api", **self.header)

        self.assertEqual(response.status_code, 200)
