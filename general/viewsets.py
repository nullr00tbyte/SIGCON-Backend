from django.contrib.auth.models import User
from rest_framework import viewsets
from general.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Entidad, Person
from .permissions import IsActive



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
    permission_classes = [IsAuthenticated, IsActive]
    queryset = Entidad.objects.all()
    serializer_class = EntidadSerializer

    def list(self, request, *args, **kwargs):
        person = Person.objects.get(pk = request.user.id)
        queryset = self.get_queryset().filter(parent__isnull=True, university=person.university)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

class UniversityViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated, IsActive]
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(owner = request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated, IsActive]
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(owner = request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class RolViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated, IsActive]
    queryset = Rol.objects.filter(is_active=True)
    serializer_class = RolSerializer

class CongresoViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated, IsActive]
    queryset = Congreso.objects.all()
    serializer_class = CongresoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(owner = request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    #Esta vista debe poder crear y editar los congresos
    def create(self, request, *args, **kwargs):
        pass

class IdTypeViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated, IsActive]
    queryset = IdentificationType.objects.filter(is_active=True)
    serializer_class = IdTypeSerializer