# accounts/factories.py
from factory.django import DjangoModelFactory
from .models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = 'testuser'
    phone = '+8613812345678'
    mfa_type = 'TOTP'