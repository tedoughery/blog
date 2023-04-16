from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h2>Blog Home</h2>')

def about(request):
    return HttpResponse('<h2>About</h2>')
