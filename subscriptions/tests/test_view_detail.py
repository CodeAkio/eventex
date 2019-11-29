from django.test import TestCase

from subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self) -> None:
        self.obj = Subscription.objects.create(
            name='Victor',
            cpf='111.222.333-44',
            email='victor@email.com',
            phone='(21) 2222-3333',
        )

        self.response = self.client.get(f'/inscricao/{self.obj.pk}/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.response.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (self.obj.name, self.obj.cpf, self.obj.email, self.obj.phone)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.response, expected)


class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get('/inscricao/0/')
        self.assertEqual(404, response.status_code)
