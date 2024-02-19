from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    message = "Welcome to our website!"  # Define the message to display
    return HttpResponse(message)