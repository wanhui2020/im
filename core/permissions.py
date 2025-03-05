# core/permissions.py
from rest_framework.permissions import BasePermission
from django.utils.translation import gettext_lazy as _

class IsSuperAdmin(BasePermission):
    message = _('Require super administrator privileges')

    def has_permission(self, request, view):
        return request.user.is_superuser