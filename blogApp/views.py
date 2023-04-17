from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'TD',
        'title': 'Test 1',
        'content': 'Hello World',
        'date_posted': 'April 17, 2023'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blogApp/home.html', context)

def about(request):
    return render(request, 'blogApp/about.html', {'title':'About'})
