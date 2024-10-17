from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

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
        subentidades = obj.subentidades.all() 
        return EntidadSerializer(subentidades, many=True).data
    
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ["id", "name", "description"]

class CongresoSerializer(serializers.ModelSerializer):
    roles = RolSerializer(many=True, read_only=True)

    class Meta:
        model = Congreso
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('initial_date') >= attrs.get('end_date'):
            raise serializers.ValidationError("La fecha de inicio debe ser anterior a la fecha de finalización.")
        return attrs
    
class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

class IdTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentificationType
        fields = '__all__'