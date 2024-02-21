from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ShoppingListForm
from .models import ShoppingList

def create_shopping_list(request):
    if request.method == 'POST':
        form = ShoppingListForm(request.POST)
        if form.is_valid():
            shopping_list = form.save()
            messages.success(request, 'Shopping list created successfully!')
            # Redirect to a success page or another view
            return redirect('create_shopping_list')  # Redirect to the shop list page after creating the shopping list
    else:
        form = ShoppingListForm()
    return render(request, 'shop_list/create_shopping_list.html', {'form': form})

'''
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def my_shop_list(request):
    return HttpResponse("Here are the shop lists!")
'''