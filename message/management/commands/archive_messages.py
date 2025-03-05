from django.core.management.base import BaseCommand
from django.utils import timezone

from message.models import Message


class Command(BaseCommand):
    help = 'Archive messages older than 30 days'

    def handle(self, *args, **kwargs):
        old_messages = Message.objects.filter(
            timestamp__lte=timezone.now() - timezone.timedelta(days=30))
        for message in old_messages:
            # 归档逻辑
            pass