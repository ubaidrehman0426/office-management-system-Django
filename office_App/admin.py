from django.contrib import admin
from .models import Role,department,Employee

# Register your models here.
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(department)
