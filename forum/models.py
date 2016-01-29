from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
# Create your models here.
from django.db import models
class Question(models.Model):
	question_text = models.CharField(max_length= 255 )
	pub_time = models.DateTimeField('pub_time')
	upvotes = models.IntegerField(default = 0)
	downvotes = models.IntegerField(default = 0)
	def __str__(self):
		return self.question_text

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer_text = models.CharField(max_length=255)
	answer_time = models.TimeField('ans_time')
	upvotes = models.IntegerField(default = 0)
	downvotes = models.IntegerField(default = 0)
	def __str__(self):
		return self.answer_text

class Qcomment(models.Model):
	cquestion = models.ForeignKey('Question', on_delete=models.CASCADE)
	qcomment_text = models.CharField(max_length=255)
	qcomment_time = models.TimeField('qcomment_time')
	def __str__(self):
		return self.qcomment_text

class Acomment(models.Model):
	answer = models.ForeignKey('Answer' , on_delete=models.CASCADE)
	acomment_text = models.CharField(max_length=255)
	acomment_time = models.DateTimeField('acomment_time')
	def __str__(self):
		return self.acomment_text

		


