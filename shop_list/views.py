from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  # Importing login_required decorator
from .forms import ShoppingListForm, ItemForm
from .models import ShoppingList, Item, ShoppingListPreference
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

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
    # Fetch private lists associated with the current user
    private_lists = ShoppingList.objects.filter(owner=request.user, is_private=True)
    
    # Fetch all public lists (including the logged-in user's public lists)
    public_lists = ShoppingList.objects.filter(is_private=False)
    
    # Combine private and public lists
    all_lists = private_lists | public_lists
    
    # Create a list of tuples containing each shopping list and the username of the owner
    lists_with_usernames = [(shopping_list, shopping_list.owner.username) for shopping_list in all_lists]
    
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

@login_required # Disable CSRF protection for this view (for demonstration purposes only)
def toggle_list_status(request, list_id):
    if request.method == 'POST':
        try:
            shopping_list = get_object_or_404(ShoppingList, pk=list_id)
            # Check if the user has a preference for the list's privacy status
            user_preference = ShoppingListPreference.objects.filter(user=request.user, shopping_list=shopping_list).first()
            if user_preference:
                # Use the user's preference if available
                shopping_list.is_private = user_preference.is_private
            else:
                # Otherwise, toggle the privacy status as before
                shopping_list.is_private = not shopping_list.is_private
            shopping_list.save()
            return JsonResponse({'status': 'success', 'is_public': not shopping_list.is_private})
        except ShoppingList.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Shopping list not found'}, status=404)
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'}, status=405)

def clone(request, list_id):
    original_list = ShoppingList.objects.get(pk=list_id)
    
    # Find the highest extension number for cloned lists
    highest_extension = ShoppingList.objects.filter(name__startswith=f"{original_list.name} (Copy)").count()
    
    # Determine the new name for the cloned list
    new_name = f"{original_list.name} (Copy{highest_extension + 1})"
    
    # Update the name of the original list
    original_list.name = new_name
    original_list.save()
    
    return redirect('show_shopping_lists')  # Redirect to the page showing all shopping lists


def rename(request, list_id):
    original_list = ShoppingList.objects.get(pk=list_id)
    
    # Find the highest extension number for cloned lists
    highest_extension = ShoppingList.objects.filter(name__startswith=f"{original_list.name} (Copy)").count()
    
    # Determine the new name for the cloned list
    new_name = f"{original_list.name} (Copy{highest_extension + 1})"
    
    # Update the name of the original list
    original_list.name = new_name
    original_list.save()
    
    return redirect('show_shopping_lists')  # Redirect to the page showing all shopping lists


def delete(request, list_id):
    original_list = ShoppingList.objects.get(pk=list_id)
    
    # Find the highest extension number for cloned lists
    highest_extension = ShoppingList.objects.filter(name__startswith=f"{original_list.name} (Copy)").count()
    
    # Determine the new name for the cloned list
    new_name = f"{original_list.name} (Copy{highest_extension + 1})"
    
    # Update the name of the original list
    original_list.name = new_name
    original_list.save()
    
    return redirect('show_shopping_lists')  # Redirect to the page showing all shopping lists

def edit_lists(request, list_id):
    shopping_list = get_object_or_404(ShoppingList, pk=list_id)
    return render(request, 'shop_list/edit_lists.html', {'shopping_list': shopping_list})










'''

@login_required
def show_shopping_lists(request):
    # Fetch private lists associated with the current user
    private_lists = ShoppingList.objects.filter(owner=request.user, is_private=True)
    
    # Fetch all public lists
    public_lists = ShoppingList.objects.filter(is_private=False)
    
    # Create a list of tuples containing each shopping list and the username of the logged-in user
    lists_with_usernames = [(shopping_list, request.user.username) for shopping_list in private_lists]
    
    # Append public lists to the list
    lists_with_usernames += [(shopping_list, shopping_list.owner.username) for shopping_list in public_lists]
    
    return render(request, 'shop_list/show_shopping_lists.html', {'lists_with_usernames': lists_with_usernames})



@login_required
def show_shopping_lists(request):
    # Fetch private lists associated with the current user
    private_lists = ShoppingList.objects.filter(owner=request.user, is_private=True)
    
    # Fetch all public lists
    public_lists = ShoppingList.objects.filter(is_private=False)
    
    # Create a list of tuples containing each shopping list and the username of the logged-in user
    lists_with_usernames = [(shopping_list, request.user.username) for shopping_list in private_lists]
    
    # Append public lists to the list
    lists_with_usernames += [(shopping_list, shopping_list.owner.username) for shopping_list in public_lists]
    
    return render(request, 'shop_list/show_shopping_lists.html', {'lists_with_usernames': lists_with_usernames})



def show_shopping_lists(request):
    # Fetch shopping lists associated with the current user
    user_shopping_lists = ShoppingList.objects.filter(owner_id=request.user.id)
    # Create a list of tuples containing each shopping list and the username of the logged-in user
    lists_with_usernames = [(shopping_list, request.user.username) for shopping_list in user_shopping_lists]
    return render(request, 'shop_list/show_shopping_lists.html', {'lists_with_usernames': lists_with_usernames})










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