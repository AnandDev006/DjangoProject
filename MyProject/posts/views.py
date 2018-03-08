from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.

def index(request):
    #return HttpResponse("Hello from posts")

    posts = Posts.objects.all()[:10]
    context = {
        'title': 'Latest Blogs',
        'posts': posts
    }

    return render( request, 'posts/index.html', context)

def details(request, pk):
    post = Posts.objects.get( id = pk )
    context = {
        'post': post
    }

    return render( request, 'posts/details.html', context)