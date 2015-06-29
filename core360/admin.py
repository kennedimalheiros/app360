from django.contrib import admin
from core360.models import Office, Department, Employee, Quiz, Evaluation
from core360.models import Question, Options
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['description', 'phone', 'active']


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = True
    verbose_name_plural = 'employee'


class UserAdmin(UserAdmin):
    inlines = (EmployeeInline, )


# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Office)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Quiz)
admin.site.register(Evaluation)
admin.site.register(Options)
admin.site.register(Question)