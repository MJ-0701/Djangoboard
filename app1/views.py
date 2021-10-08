from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world")

# def home(request):
#     template = loader.get_template('app1/index.html')
#     return HttpResponse(template.render(request))

def home(request):
    return render(request, 'index.html')


def user(request):
    return render(request, 'user/user.html')
