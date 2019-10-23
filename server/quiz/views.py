from django import forms
from django.http import Http404
from django.shortcuts import render

from time import sleep

'''
This fn. retrieves the data from quiz form
    '''
def get_inputs(request):
    if request.method == 'POST':
        print(request.POST)

    '''
This fn. is used to check if the input is correct. (i.e., check if the user 
entered any characters in place of integers, etc)
    '''
def validate_inputs(request):
    pass

    '''
This fn. cleans up inputs and formats it so the model can run through the data without a problem
    '''
def sanitize_inputs():
    pass  

    '''
This function creates the ML model
    '''
def get_model():
    pass

    '''
We use dummy data with target labels to train the ML model
    '''
def train_model():
    pass

    ''' 
We run the ML model on the validated and sanitized inputs to get our results
    '''
def inference():
    pass


# Create your views here.
def quiz_view(request):
    # check if this is a HTTP POST request, then process the quiz data
    if request.method != 'POST':
        raise Http404()

    # FIXME remove this when we have an actual implementation
    sleep(0.25) # pretend that we are actually doing work
 
    context = {}
    return render(request, 'quiz/quiz_results.html', context)
