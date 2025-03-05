from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'group', 'message_type', 'content', 'timestamp', 'is_read', 'is_delivered']