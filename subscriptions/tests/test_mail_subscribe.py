from django.core import mail
from django.shortcuts import resolve_url
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self) -> None:
        data = dict(name='Victor Siqueira', cpf='111.222.333-44', email='victor@email.com', phone='(21) 2222-3333')
        self.client.post(resolve_url('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'victor@email.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Victor Siqueira',
            '111.222.333-44',
            'victor@email.com',
            '(21) 2222-3333',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
