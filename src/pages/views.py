from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.


def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})

def contacts_view(request, *args, **kwargs):
	return render(request, "contacts.html", {})


def about_view(request, *args, **kwargs):

	
	return render(request, "about.html", {})

def social_view(request, *args, **kwargs):
	return render(request, "social.html", {})
 