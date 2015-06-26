from django.contrib import admin
from models import Office
from core360.models import Department
from models import Employee

# Register your models here.
admin.site.register(Office)
admin.site.register(Department)
admin.site.register(Employee)