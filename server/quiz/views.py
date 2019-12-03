from django import forms
from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponseRedirect

from time import sleep

import numpy as np
from mxnet import nd, ndarray, gluon, autograd
from mxnet.gluon import nn

from smart_city_finder.views import home # for homepage redirection


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
    return nd.sigmoid(model(user_input)).asnumpy().tolist()[0]


def format_output(ratings, preferred_cities=None):
    default_cities = [
        'Austin', 'Buffalo', 'Dallas', 'Denver', 'Los Angeles',
        'New York City', 'San Francisco', 'San Jose', 'Seattle'
    ]

    candidate_cities = []

    if preferred_cities is not None:
        count = len(preferred_cities)
        assert(count <= 9)
        candidate_cities = preferred_cities + default_cities[count:]
    else:
        candidate_cities = default_cities

    result = dict(zip(candidate_cities, ratings))
    return result


# Create your views here.
def quiz_view(request):
    # check if this is a HTTP POST request, then process the quiz data
    if request.method != 'POST':
        # Instead of raising Http404 exception,
        # simply redirect user back to the homepage
        return home(request)

    model = retrieve_model()
    input = retrieve_user_input(request)
    ratings = inference(model, input)

    # FIXME:
    #   Improve quiz form so that user's preferred cities can be retrieved below
    preferred_cities = None
    result = format_output(ratings, preferred_cities)
    print(result)
    sleep(3)

    # FIXME:
    #   Improve result presentation page such that result
    #   can be rendered as a list of cities along with its ratings
    return HttpResponseRedirect(request.path_info)
