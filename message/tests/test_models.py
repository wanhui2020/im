from django.test import TestCase
from accounts.models import User
from message.models import Message


class MessageTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='user1')
        self.user2 = User.objects.create(username='user2')

    def test_message_creation(self):
        message = Message.objects.create(
            sender=self.user1,
            receiver=self.user2,
            content='Hello')
        self.assertEqual(message.content, 'Hello')