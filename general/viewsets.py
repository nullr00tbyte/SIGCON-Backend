from django.contrib.auth.models import User
from rest_framework import viewsets
from general.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Entidad, Person

class UserViewSet(viewsets.ViewSet):
    """
    Vista de los datos del usuario logueado
    """
    permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = User.objects.get(pk = request.user.id)
        serializer = UserSerializer(queryset)
        return Response(serializer.data)

class EntidadViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Vista las entidades registradas para la universidad del usuario logueado
    """
    permission_classes = [IsAuthenticated]
    queryset = Entidad.objects.all()
    serializer_class = EntidadSerializer

    def list(self, request, *args, **kwargs):
        person = Person.objects.get(pk = request.user.id)
        queryset = self.get_queryset().filter(parent__isnull=True, university=person.university)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)