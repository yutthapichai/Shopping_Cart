from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    text_var = 'this is my first jungo app web page.'
    return HttpResponse(text_var)
