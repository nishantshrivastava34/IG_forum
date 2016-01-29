from django.shortcuts import render
from django.http import	HttpResponse
from django.shortcuts import render , get_object_or_404
from .models import Question


'''#This will show recent questions , signup ,signin options 
(no of answers, no of votes,no of comments,time published , published by ,) for questions '''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_time')[:10]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'forum/index.html', context)


'''This will show particular question text , publishion time of question ,
user who published , Commenting on question ,show comments , upvotes , downvote on question.


Show Top answers with upvotes 
votes on answers
comments on answers
add answers.'''
def detail(request,question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request , 'forum/detail.html' , {'question' : question})

