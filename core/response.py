# core/response.py
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _


class LocalizedResponse(Response):
    def __init__(self, data=None, **kwargs):
        if isinstance(data, dict):
            data = {key: _(value) if isinstance(value, str) else value
                    for key, value in data.items()}
        super().__init__(data, **kwargs)
