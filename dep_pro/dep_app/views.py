from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def welcome():
    return HttpResponse("from the server")
