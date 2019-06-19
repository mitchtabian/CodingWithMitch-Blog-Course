from django.db import models

# #Two tuple structure
# #The first element in each tuple is the value that will be stored in the database. The second element is displayed by the field’s form widget.
# #Tuple
# PRIORITY = [
# 	('L', 'Low'), #Tuple1
# 	('M', 'Medium'), #Tuple2
# 	('H', 'High'), #Tuple3
# ]

# class Question(models.Model):
# 	title		 			= models.CharField(max_length=60)
# 	question 				= models.TextField(max_length=400)
# 	priority 				= models.CharField(max_length=1, choices=PRIORITY)

# 	def __str__(self):
# 		return self.title


# 	class Meta:
# 		verbose_name = 'The Question'
# 		verbose_name_plural = 'Questions from People'