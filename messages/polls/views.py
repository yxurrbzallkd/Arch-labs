from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def stump(request):
	return HttpResponse("Hello from messages server! Not implemented.")
