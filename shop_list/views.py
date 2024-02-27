from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # Importing login_required decorator
from .forms import ShoppingListForm, ItemForm
from .models import ShoppingList, Item
from django.contrib.auth.models import User

def index(request):
    return render(request, 'shop_list/index.html')

@login_required # Applying login_required decorator
def create_shopping_list(request):
    if request.method == 'POST':
        form = ShoppingListForm(request.POST)
        if form.is_valid():
            shopping_list = form.save(commit=False)
            shopping_list.owner_id = request.user.id  # Set owner_id to the ID of the logged-in user
            shopping_list.save()
            messages.success(request, 'Shopping list created successfully!')
            return redirect('create_shopping_list')
    else:
        form = ShoppingListForm()
    return render(request, 'shop_list/create_shopping_list.html', {'form': form})

@login_required
def show_shopping_lists(request):
    # Fetch shopping lists associated with the current user
    user_shopping_lists = ShoppingList.objects.filter(owner_id=request.user.id)
    # Create a list of tuples containing each shopping list and the username of the logged-in user
    lists_with_usernames = [(shopping_list, request.user.username) for shopping_list in user_shopping_lists]
    return render(request, 'shop_list/show_shopping_lists.html', {'lists_with_usernames': lists_with_usernames})

#@login_required  # Applying login_required decorator
def add_item(request, list_id):
    shopping_list = ShoppingList.objects.get(pk=list_id)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.shopping_list = shopping_list
            item.save()
            return redirect('show_shopping_lists')
    else:
        form = ItemForm()
    return render(request, 'shop_list/add_item.html', {'form': form, 'shopping_list': shopping_list})

#login_required  # Applying login_required decorator
def show_items(request, list_id):
    shopping_list = ShoppingList.objects.get(pk=list_id)
    items = Item.objects.filter(shopping_list=shopping_list)
    return render(request, 'shop_list/show_items.html', {'shopping_list': shopping_list, 'items': items})

'''
@login_required
def show_shopping_lists(request):
    # Fetch shopping lists associated with the current user
    user_shopping_lists = ShoppingList.objects.filter(owner_id=request.user.id)
    return render(request, 'shop_list/show_shopping_lists.html', {'lists_with_usernames': user_shopping_lists})


@login_required
def show_shopping_lists(request):
    # Fetch shopping lists associated with the current user
    user_shopping_lists = ShoppingList.objects.filter(owner_id=request.user.id)
    return render(request, 'shop_list/show_shopping_lists.html', {'lists_with_usernames': user_shopping_lists})

def show_shopping_lists(request):
    # Fetch all shopping lists from the database
    lists_with_usernames = []
    for shopping_list in ShoppingList.objects.all():
        owner_username = User.objects.get(pk=shopping_list.owner_id).username
        lists_with_usernames.append((shopping_list, owner_username))
    return render(request, 'shop_list/show_shopping_lists.html', {'lists_with_usernames': lists_with_usernames})







def create_shopping_list(request):
    if request.method == 'POST':
        form = ShoppingListForm(request.POST)
        if form.is_valid():
            shopping_list = form.save(commit=False)
            owner_id = 4
            shopping_list.owner = User.objects.get(pk=owner_id)
            shopping_list.save()
            messages.success(request, 'Shopping list created successfully!')
            return redirect('create_shopping_list')
    else:
        form = ShoppingListForm()
    return render(request, 'shop_list/create_shopping_list.html', {'form': form})

@login_required  # Applying login_required decorator
def show_shopping_lists(request):
    lists = ShoppingList.objects.all()  # Fetch all shopping lists from the database
    return render(request, 'shop_list/show_shopping_lists.html', {'lists': lists})

def show_shopping_lists(request):
    # Retrieve shopping lists associated with the current user
    lists = ShoppingList.objects.filter(owner=request.user)
    return render(request, 'shop_list/show_shopping_lists.html', {'lists': lists})







from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def my_shop_list(request):
    return HttpResponse("Here are the shop lists!")
'''