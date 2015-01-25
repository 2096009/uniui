from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says: Hello world! <br/> <a href='/rango/about'>About</a>")
	
def about(request):
	return HttpResponse("Rango says here is the about page. This tutorial has been put together by Tautvydas Rutkauskas, 2096009 <a href='/rango/'>Rango</a>")