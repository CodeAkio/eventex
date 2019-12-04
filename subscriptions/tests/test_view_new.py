from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url

from subscriptions.forms import SubscriptionForm
from subscriptions.models import Subscription


class SubscriptionNewGet(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get(resolve_url('subscriptions:new'))

    def test_get(self):
        """Get /inscricao/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        """Html must contain input tags"""
        tags = (
            ('<form', 1),
            ('<input', 6),
            ('type="text"', 3),
            ('type="email"', 1),
            ('type="submit"', 1),
        )

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscriptionNewPostValid(TestCase):
    def setUp(self) -> None:
        data = dict(name='Victor Siqueira', cpf='11122233344', email='victor@email.com', phone='(21) 2222-3333')
        self.response = self.client.post(resolve_url('subscriptions:new'), data)

    def test_post(self):
        """Valid POST should redirect to /inscricao/86a04bab-a8be-4d49-8c0e-11ae0c11daf9/"""
        hashid = self.response.context['subscription'].hashid
        self.assertRedirects(self.response, resolve_url('subscriptions:detail', hashid))

    def test_send_subscribe_email(self):
        """Must send e-mail"""
        self.assertEqual(1, len(mail.outbox))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())


class SubscriptionNewInvalid(TestCase):
    def setUp(self) -> None:
        self.response = self.client.post(resolve_url('subscriptions:new'), {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())


class TemplateRegressionTest(TestCase):
    def test_template_has_non_field_errors(self):
        invalid_data = dict(name='Victor', cpf='11122233344')
        response = self.client.post(resolve_url('subscriptions:new'), invalid_data)

        self.assertContains(response, '<ul class="errorlist nonfield">')
