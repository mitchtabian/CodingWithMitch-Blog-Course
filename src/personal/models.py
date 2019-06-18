from django.db import models


PRIORITY = [
	("H", "High"),
	("M", "Medium"),
	("L", "Low"),
]

class Question(models.Model):
	title 					= models.CharField(max_length=60)
	question 				= models.TextField(max_length=400)
	priority 				= models.CharField(max_length=1, choices=PRIORITY)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "The Question"
		verbose_name_plural = "Peoples Questions"


