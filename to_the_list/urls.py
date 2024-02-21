"""
URL configuration for to_the_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user_authentication import views
from shop_list.views import create_shopping_list
from shop_list.views import show_shopping_lists


urlpatterns = [
    path('', views.home, name='home'),  # Map the home view to the root URL
    path('admin/', admin.site.urls),
    path('shop_list/create/', create_shopping_list, name='create_shopping_list'),
    path('shop_list/', show_shopping_lists, name='show_shopping_lists'),
]

'''
   path('shop_list/', my_shop_list, name='shop_list'),   # Admin URL remains unchanged
'''