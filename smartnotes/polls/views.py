from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    #html = "<html><head><title>Polls Page</title></head><body><h1>This Page will show polls</h1></body></html>"
    question_list = Question.objects.order_by('-timing')[:]
    questions = {
        'question_list' : question_list,

    }
    return render(request,'polls/index.html',questions)


def detail(request,id):
    return HttpResponse("<html><head><title>Detailed Question</title></head><body><h1>Here is your Question Page Now tell me more about this</h1></body></html>")