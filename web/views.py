from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def page(request):
	return HttpResponse('hello world')