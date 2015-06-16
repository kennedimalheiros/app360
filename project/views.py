from django.http import HttpResponse


def home(request):
	return HttpResponse('Avaliacao 360')