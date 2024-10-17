from rest_framework import permissions
from .models import Person
from rest_framework.exceptions import PermissionDenied

class IsActive(permissions.BasePermission):
    """
    Verifica que el usuario este activo en la base de datos
    """

    def has_permission(self, request, view):
        person = Person.objects.get(pk = request.user.id)
        if not person.is_active:
            raise PermissionDenied("El usuario no esta activo")