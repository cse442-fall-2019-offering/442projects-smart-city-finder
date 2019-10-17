from django import forms
from django.http import Http404
from django.shortcuts import render

from time import sleep

# Create your views here.

def quiz_view(request):
    # check if this is a HTTP POST request, then process the quiz data
    if request.method != 'POST':
        raise Http404()

    # FIXME remove this when we have an actual implementation
    sleep(0.25) # pretend that we are actually doing work

    context = {}
    return render(request, 'quiz/quiz_results.html', context)
