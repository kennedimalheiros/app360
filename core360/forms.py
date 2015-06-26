from django.forms import ModelForm
from core360.models import Department


class DepartmentForm(ModelForm):
	class Meta:
		model = Department
		fields = ['description', 'phone'] 