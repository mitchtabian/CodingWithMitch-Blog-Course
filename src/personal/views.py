from django.shortcuts import render

from personal.models import Question

def home_screen_view(request):
	context = {}
	# context['some_string'] = "this is some string that I'm passing to the view"

	# context = {
	# 	'some_string': "this is some string that I'm passing to the view"
	# }

	# context['some_number'] = 3151351

	# list_of_values = []
	# list_of_values.append("first entry")
	# list_of_values.append("second entry")
	# list_of_values.append("third entry")
	# list_of_values.append("fourth entry")
	# list_of_values.append("fifth entry")
	# context['list_of_values'] = list_of_values


	questions = Question.objects.all()
	context['questions'] = questions

	return render(request, "personal/home.html", context)