from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Пермишен проверки пользователя на владельца"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user
