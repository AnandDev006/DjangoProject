from django.shortcuts import render, redirect

from .models import articleContent

from .forms import BlogForm

# Create your views here.

def index(request):
	blog_article = articleContent.objects.order_by('-date_added')
	context = { 'articles' : blog_article }
	return render( request, 'article/index.html', context)

def blogform(request):
	if request.method == 'POST':
		form = BlogForm(request.POST)

		if form.is_valid():
			new_req = articleContent( articleTitle = request.POST['articleName'], articleBody = request.POST['articleBody'])
			new_req.save()
			return redirect('index')

	else:
		form = BlogForm()

	context = { 'form' : form }

	return render( request, 'article/blogform.html', context)