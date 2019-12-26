from datetime import datetime

from django.shortcuts import resolve_url
from django.test import TestCase

from subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self) -> None:
        self.obj = Subscription(
            name='Victor',
            cpf='11122233344',
            email='victor@email.com',
            phone='(21) 2222-3333'
        )

        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual("Victor", str(self.obj))

    def test_paid_default_to_false(self):
        """By default paid must be False."""
        self.assertEqual(False, self.obj.paid)

    def test_get_absolute_url(self):
        url = resolve_url('subscriptions:detail', self.obj.hashid)
        self.assertEqual(url, self.obj.get_absolute_url())
