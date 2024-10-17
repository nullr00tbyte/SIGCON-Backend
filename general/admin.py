from django.contrib import admin
from .models import *

admin.site.site_header = 'SIGCON'
admin.site.register(Entidad)
admin.site.register(Person)
admin.site.register(Congreso)
admin.site.register(Rol)
admin.site.register(University)