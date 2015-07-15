from django.contrib import admin
from core360.models import Office, Department, Employee, Quiz, Evaluation
from core360.models import Question, Options, Answer
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

class RatingAdmin(admin.ModelAdmin):
    model = Evaluation
    list_display = ('id', 'description')
   # exclude = ['categories']


    def save_model(self, request, obj, form, change):
        super(RatingAdmin, self).save_model(request, obj, form, change)
        obj.save()
        form.save_m2m()
        
        # Verify if obj is a new tuple
        if not change:
            for question in obj.questions.all():
                answer = Answer(question=question, evaluation=obj)
                answer.save()

class AnswerAdmin(admin.ModelAdmin):
    model = Answer
    list_display = ('evaluation', 'question', 'have_answer')

    def have_answer(self, obj):
        return 'Pendente' if obj.answer == None else 'Respondida'

# Register your models here.
admin.site.register(Department, DepartmentAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Evaluation, RatingAdmin)
admin.site.register(Question)
admin.site.register(Options)
admin.site.register(Answer, AnswerAdmin )
admin.site.register(Office)
admin.site.register(Employee)
admin.site.register(Quiz)

