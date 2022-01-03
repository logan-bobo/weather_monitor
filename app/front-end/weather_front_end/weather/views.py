import requests
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # get the list of todos
    response = requests.get('http://127.0.0.1:8000/location/53.480837/-2.244914')
    # transfor the response to json objects
    weather = response.json()
    return render(request, "home.html", {"temperature": weather})
