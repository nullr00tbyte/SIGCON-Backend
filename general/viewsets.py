from django.contrib.auth.models import User
from rest_framework import viewsets
from general.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    permission_classes = [IsAuthenticated]
    def list(self, request):
        queryset = User.objects.get(pk = request.user.id)
        serializer = UserSerializer(queryset)
        return Response(serializer.data)
