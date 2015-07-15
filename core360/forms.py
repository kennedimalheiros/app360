from django.forms import ModelForm
from core360.models import Department
from django.forms import RadioSelect
from django import forms
from core360.models import Office, Department, Employee, Quiz, Evaluation
from core360.models import Question, Options, Answer

class DepartmentForm(ModelForm):
	class Meta:
		model = Department
		fields = ['description', 'phone'] 

class FormQuestion(forms.ModelForm):
    options = forms.ModelMultipleChoiceField(
        widget=forms.RadioSelect,
        queryset=[])
    class Meta:
        model = Question
        fields = ('text', 'options',)


    def __init__(self, *args, **kwargs):
        super(FormQuestion, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['options'].queryset = Question.objects.get(
                pk=self.instance.pk).options.all()

class FormAnswer(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('evaluation', 'question','answer')

    def __init__(self, *args, **kwargs):
        super(FormAnswer, self).__init__(*args, **kwargs)

        self.fields['answer'].widget = forms.RadioSelect()
        self.fields['answer'].empty_label=None
        self.fields['answer'].queryset = Answer.objects.get(
           pk=self.instance.pk).question.options.all()
        self.fields['evaluation'].widget.attrs['readonly'] = True
        self.fields['question'].widget.attrs['readonly'] = True
#class FormRating(forms.ModelForm):
  #  class Meta:
  #      model = Evaluation
   #     fields = ('strong_points', 'need_improvement')