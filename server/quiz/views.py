from django import forms
from django.http import Http404
from django.shortcuts import render

# Create your views here.

def quiz_view(request):
    # check if this is a HTTP POST request, then process the quiz data
    raise Http404()
    # return render(request, 'quiz/quiz.html')
