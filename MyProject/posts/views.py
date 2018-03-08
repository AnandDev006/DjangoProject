from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Posts
from .forms import BlogForm

# Create your views here.

def index(request):

    posts = Posts.objects.all()[:10]
    context = {
        'title': 'Latest Blogs',
        'posts': posts
    }

    return render( request, 'posts/index.html', context)

def bloginput(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            new_req = Posts( title = request.POST['blogName'], body = request.POST['blogBody'])
            new_req.save()
            return redirect('index')
        
    else:
        form = BlogForm()
    
    context = {
        'form': form
    }

    return render( request, 'posts/bloginput.html', context)

def details(request, pk):
    post = Posts.objects.get( id = pk )
    context = {
        'post': post
    }

    return render( request, 'posts/details.html', context)