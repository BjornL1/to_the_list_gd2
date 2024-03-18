from django.shortcuts import render
from django.http import HttpResponse

def learn_view(request):
    return render(request, 'learn.html')

def error_view(request):
    # Intentionally raise an exception
    raise Exception("Intentional server error")

def error_404_view(request, exception):
    # Return the 404 error page template
    return render(request, '404.html', status=404)