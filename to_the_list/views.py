from django.shortcuts import render

def learn_view(request):
    return render(request, 'learn.html')