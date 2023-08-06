from time import time

from unittest import skip

from django.test import TestCase
from django.core.exceptions import ValidationError

from netbox_data_disk.models import NameServer, Record, RecordTypeChoices, Zone


class AutoSOASerialTest(TestCase):

    zone_data = {
        "default_ttl": 86400,
        "soa_rname": "hostmaster.example.com",
        "soa_refresh": 172800,
        "soa_retry": 7200,
        "soa_expire": 2592000,
        "soa_ttl": 86400,
        "soa_minimum": 3600,
        "soa_serial": 1,
    }

    @classmethod
    def setUpTestData(cls):
        cls.start_time = int(time())

        cls.nameserver = NameServer.objects.create(name="ns1.example.com")

        cls.zones = [
            Zone(
                name="zone1.example.com",
                **cls.zone_data,
                soa_mname=cls.nameserver,
                soa_serial_auto=True,
            ),
            Zone(
                name="zone2.example.com",
                **cls.zone_data,
                soa_mname=cls.nameserver,
                soa_serial_auto=False,
            ),
            Zone(
                name="1.0.10.in-addr.arpa",
                **cls.zone_data,
                soa_mname=cls.nameserver,
                soa_serial_auto=True,
            ),
            Zone(
                name="2.0.10.in-addr.arpa",
                **cls.zone_data,
                soa_mname=cls.nameserver,
                soa_serial_auto=False,
            ),
        ]
        for zone in cls.zones:
            zone.save()

    def test_soa_serial_auto(self):
        zone = self.zones[0]
        zone.save()

        self.assertTrue(int(zone.soa_serial) >= self.start_time)

    def test_soa_serial_fixed(self):
        zone = self.zones[1]
        zone.save()

        self.assertEqual(zone.soa_serial, 1)

    def test_change_to_soa_serial_auto(self):
        zone = self.zones[1]
        zone.save()

        zone.soa_serial_auto = True
        zone.save()

        self.assertTrue(int(zone.soa_serial) >= self.start_time)

    def test_change_to_soa_serial_fixed(self):
        zone = self.zones[0]
        zone.save()

        zone.soa_serial_auto = False
        zone.soa_serial = 42
        zone.save()

        self.assertEqual(zone.soa_serial, 42)

    @skip("This test still has timing issues")
    def test_create_ptr_soa_serial_auto(self):
        f_zone = self.zones[0]
        r_zone = self.zones[2]

        f_record = Record(
            zone=f_zone,
            name="name1",
            type=RecordTypeChoices.A,
            value="10.0.1.42",
            ttl=86400,
        )
        f_record.save()

        f_zone.refresh_from_db()
        r_zone.refresh_from_db()

        self.assertTrue(int(r_zone.soa_serial) >= int(f_zone.soa_serial))

    def test_create_ptr_soa_serial_fixed(self):
        f_zone = self.zones[0]
        r_zone = self.zones[3]

        f_record = Record(
            zone=f_zone,
            name="name1",
            type=RecordTypeChoices.A,
            value="10.0.2.42",
            ttl=86400,
        )
        f_record.save()

        r_record = Record.objects.get(
            type=RecordTypeChoices.PTR,
            value=f"{f_record.name}.{f_zone.name}.",
            zone=r_zone,
        )
        r_zone = Zone.objects.get(pk=r_record.zone.pk)

        self.assertEqual(r_zone.soa_serial, 1)

    def test_missing_soa_serial(self):
        zone = self.zones[0]
        zone.soa_serial = None
        zone.soa_serial_auto = False

        with self.assertRaises(ValidationError):
            zone.save()
