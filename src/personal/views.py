from django.shortcuts import render
from personal.models import Question


def home_screen_view(request):
	
	context = {}
	questions = Question.objects.all()
	context['questions'] = questions

	return render(request, "personal/home.html", context)
