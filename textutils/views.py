from http.client import ImproperConnectionState
from django import http

def index(request):
    return http.HttpResponse("Hello world")