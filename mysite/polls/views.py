from django.shortcuts import render

# Create your views here.
from django.https import HttpsResponse


def index(request):
    return HttpsResponse("Hello, world. You're at the polls index.")