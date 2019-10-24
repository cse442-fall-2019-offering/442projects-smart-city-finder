from django.shortcuts import render

def terms(request):
    return render(request, 'terms.html', context={})

def privacy(request):
    return render(request, 'privacy.html', context={})

def home(request):
    return render(request, 'index.html', context={})
