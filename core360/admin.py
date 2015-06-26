from django.contrib import admin
from core360.models import Office
from core360.models import Department
from core360.models import Employee

# Register your models here.
admin.site.register(Office)
admin.site.register(Department)
admin.site.register(Employee)