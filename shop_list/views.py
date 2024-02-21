from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def my_shop_list(request):
    return HttpResponse("Here are the shop lists!")