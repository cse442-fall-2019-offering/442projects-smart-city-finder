# Welcome to CSE442
This is to create a file so that your repo has a place to start.

# Developer Quick Start

## For Windows

First, make sure you've installed Python 3.

Then open a terminal and do the following:

(make sure you used `cd` to enter the directory you cloned the project's repository into)

Then, in a the terminal, create a virtual environment:

    python -m venv env

Install the project's dependencies:

    .\env\Scripts\pip.exe install -r requirements.txt

You can then start Django's built-in development server:

    .\env\Scripts\python.exe .\server\manage.py runserver
