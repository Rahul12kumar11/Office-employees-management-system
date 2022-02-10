from django.contrib import admin
from .models import Employees, Department, role, Contact

# Register your models here.
admin.site.register(Employees)
admin.site.register(Department)
admin.site.register(role)
admin.site.register(Contact)
