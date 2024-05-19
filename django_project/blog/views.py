from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts=[
    {
        'author': 'Deep Shikhar',
        'title':'Book1',
        'content':'First post content',
        'date_Posted':'August 27,2018'
    },
    {
        'author': 'Him Shikhar',
        'title':'Book2',
        'content':'Second post content',
        'date_Posted':'August 28,2018'
    }
]


def home(request):
    context = {
        'posts':posts
        }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})