from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Alessandra',
        'title': 'First Blog Post',
        'content': 'Content for the first post',
        'date_posted': '10/12/2023' 
    },

    {
        'author': 'John',
        'title': 'Second Blog Post',
        'content': 'Content for the second post',
        'date_posted': '11/12/2023'
    },

    {
        'author': 'Paul',
        'title': 'Third Blog Post',
        'content': 'Content for the third post',
        'date_posted': '12/12/2023'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})