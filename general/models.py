from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from .mixins import flags
from django_countries.fields import CountryField

class IdentificationType(flags):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class University(flags):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Entidad(flags):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subentidades')
    created_at = models.DateTimeField(auto_now_add=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Person(flags):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, null=True, blank=True)
    type_identification = models.ForeignKey(IdentificationType, on_delete=models.CASCADE, null=True, blank=True)
    identification = models.CharField(max_length=50, unique=True, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="person_owner", null=True, blank=True)
    country = CountryField(default='HN')
    def __str__(self):
        return f"{self.user.email}"

class Rol(flags):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class Congreso(flags):
    university = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    initial_date = models.DateField()
    end_date = models.DateField()
    place = models.ForeignKey(Entidad, on_delete=models.CASCADE, related_name="congress_places")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    roles = models.ManyToManyField(Rol, related_name="congress_roles")
    def clean(self):
        if self.initial_date >= self.end_date:
            raise ValidationError("La fecha de inicio debe ser anterior a la fecha de finalización.")

    def is_active_congreso(self):
        return self.is_active and self.initial_date <= timezone.now().date() <= self.end_date

    def __str__(self):
        return self.name
