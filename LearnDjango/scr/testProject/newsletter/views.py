from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm

# Create your views here.

def index(request):
    title = "My Title"
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        saved_form = form.save(commit = False)
        saved_form.save()
    context = {
        "title": title,
        "form": form,
    }
    return render( request, 'newsletter/index.html', context)
