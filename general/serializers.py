from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Entidad

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "last_login", "first_name", "last_name"]

class EntidadSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Entidad
        fields = ['id', 'name', 'children']

    def get_children(self, obj):
        subentidades = obj.subentidades.all()  # Obtiene las subentidades relacionadas
        return EntidadSerializer(subentidades, many=True).data