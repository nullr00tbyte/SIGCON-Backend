from rest_framework import permissions
from .models import Person
from rest_framework.exceptions import PermissionDenied

class IsActive(permissions.BasePermission):
    """
    Verifica que el usuario esté activo en la base de datos.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        try:
            person = Person.objects.get(pk=request.user.id)
        except Person.DoesNotExist:
            raise PermissionDenied("El usuario no esta registrado")
        
        if not person.is_active:
            raise PermissionDenied("El usuario no está activo")
        
        return True
