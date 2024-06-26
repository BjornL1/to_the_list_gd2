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
from django.urls import path, include
from shop_list.views import create_shopping_list
from shop_list.views import show_shopping_lists, edit_item, item_rename, duplicate_item, delete_item
from shop_list.views import add_item, show_items, index, toggle_list_status, edit, clone, rename, delete, toggle_item_done
from django.urls import path
from . import views
from django.views.defaults import page_not_found
from shop_list.views import index

urlpatterns = [
    path('', index, name='home'), # Map the home view to the root URL
    path('admin/', admin.site.urls),
    path('shop_list/create/', create_shopping_list, name='create_shopping_list'),
    path('shop_list/', show_shopping_lists, name='show_shopping_lists'),
    path('shop_list/<int:list_id>/add_item/', add_item, name='add_item'),
    path('shop_list/<int:list_id>/', show_items, name='show_items'),
    path('accounts/', include('allauth.urls')),
    path('toggle-list-status/<int:list_id>/', toggle_list_status, name='toggle_list_status'),
    path('shop_list/<int:list_id>/edit/', edit, name='edit'),
    path('shop_list/<int:list_id>/clone/', clone, name='clone'),
    path('shop_list/<int:list_id>/rename/', rename, name='rename'),  # Define the URL pattern for renaming the list
    path('shop_list/<int:list_id>/delete/', delete, name='delete'),  # Define the URL pattern for renaming the list
    path('toggle-item-done/<int:item_id>/', toggle_item_done, name='toggle_item_done'),
    path('shop_list/edit_item/<int:item_id>/', edit_item, name='edit_item'),
    path('shop_list/<int:item_id>/item_rename/', item_rename, name='rename_item'),
    path('shop_list/<int:item_id>/duplicate_item/', duplicate_item, name='duplicate_item'),
    path('shop_list/<int:item_id>/delete_item/', delete_item, name='delete_item'),
    path('learn/', views.learn_view, name='learn'),
    path('error/', views.error_view, name='error'),
]

handler404 = 'to_the_list.views.error_404_view'


 