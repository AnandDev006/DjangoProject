from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def MyResponse(request):
	return HttpResponse('Sup Dude \n Whatcha upto ?')