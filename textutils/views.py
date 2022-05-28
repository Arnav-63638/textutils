from http.client import ImproperConnectionState
from django import http

def index(request):
    return http.HttpResponse("Hello world")
def capitalise(request):
    return http.HttpResponse("Hello Arnav")
