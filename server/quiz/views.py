from django import forms
from django.http import Http404
from django.shortcuts import render

from time import sleep

import numpy as np
from mxnet import nd, ndarray, gluon, autograd
from mxnet.gluon import nn

def retrieve_user_input(request):
    '''
    Retrieve user inputted data from quiz form.
    param:
        request -> A POST request object containing user inputted data as
        key:value pairs
    result -> A numpy array of shape (1, 1, 9) with numerical features.
    '''
    # if request.method == 'POST':
    #     print(request.POST)

    input = np.random.randint(0, 1, size=(1, 1, 9))
    valid = validate_user_input(input)
    if not valid:
        #FIXME: Define output when user input is not valid.
        pass

    result = sanitize_user_input(input)
    return result


def validate_user_input(input):
    '''
    Check if the input is correct. (i.e., check if the user
    entered any characters in place of integers, etc)
    '''
    #FIXME: Define actual validation process.
    return True


def sanitize_user_input(input):
    '''
    Clean up user input so convert it into a format suitable for inference.
    '''
    #FIXME: Define actual data sanitization process.
    return input


def retrieve_model():
    '''
    Retrieve the multi-layer perceptron (MLP) model for later use.
    '''

    mlp = nn.Sequential()

    mlp.add(nn.Dense(256, activation="relu"),
            nn.Dense(128, activation="relu"),
            nn.Dense(64, activation="relu"),
            nn.Dense(32, activation="relu"),
            nn.Dense(9))

    mlp.initialize()
    return mlp


def train_model(model, data):
    '''
    Train the MLP on dummy data.
    '''
    pass


def inference(model, user_input):
    '''
    Run the MLP on user input to get prediction.
    '''
    user_input = nd.array(user_input)
    return nd.softmax(model(user_input))[0]


# Create your views here.
def quiz_view(request):
    # check if this is a HTTP POST request, then process the quiz data
    if request.method != 'POST':
        raise Http404()

    model = retrieve_model()
    input = retrieve_user_input(request)
    probabilities = inference(model, input)
    print(probabilities)
    
    # FIXME:
    # finalize the city of choice based on the probabilities
    # and then present it on the resulting page
    sleep(3)

    context = {}
    return render(request, 'quiz/quiz_results.html', context)
