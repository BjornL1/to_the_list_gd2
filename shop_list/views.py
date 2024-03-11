from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  # Importing login_required decorator
from .forms import ShoppingListForm, ItemForm
from .models import ShoppingList, Item, ShoppingListPreference
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseForbidden
from django.utils.text import slugify



def index(request):
    return render(request, 'shop_list/index.html')

@login_required
def create_shopping_list(request):
    # Clear any existing messages if the user is authenticated
    if request.user.is_authenticated:
        storage = messages.get_messages(request)
        new_messages = []
        for message in storage:
            if "You have signed out." not in message.message and "Successfully signed in as" not in message.message:
                new_messages.append(message)
        # Replace the messages in the storage with the filtered messages
        request._messages._loaded_data = new_messages

    if 'form_page_visited' in request.session:
        del request.session['form_page_visited']
        
    if request.method == 'POST':
        form = ShoppingListForm(request.POST)
        if form.is_valid():
            shopping_list = form.save(commit=False)
            shopping_list.owner_id = request.user.id  
            shopping_list.save()
            shopping_list_name = shopping_list.name
            messages.success(request, f'Shopping list "{shopping_list_name}" created successfully!')
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

    # Check if the current user is the owner of the list
    is_owner = shopping_list.owner == request.user

    if request.method == 'POST':
        # Handle checkbox state changes
        item_ids = request.POST.getlist('item_ids')  
        for item_id in item_ids:
            item = Item.objects.get(pk=item_id)
            item.is_done = not item.is_done  # Toggle the state of the checkbox
            item.save()  # Save the changes to the database

    return render(request, 'shop_list/show_items.html', {'shopping_list': shopping_list, 'items': items, 'is_owner': is_owner})

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

@login_required
def clone(request, list_id):
    original_list = ShoppingList.objects.get(pk=list_id)
    
    # Clone the list
    cloned_list = ShoppingList.objects.create(
        name=f"{original_list.name} (Copy)",
        owner=request.user,  # Set the owner to the current user
        is_private=original_list.is_private
    )
    # Increment the clone count
    original_list.clone_count += 1
    original_list.save()

    # Optionally, you can also copy the items from the original list to the cloned list
    for item in original_list.item_set.all():
        cloned_item = Item.objects.create(
            name=item.name,
            quantity=item.quantity,
            shopping_list=cloned_list
        )

    return redirect('show_shopping_lists')
    
@login_required
def rename(request, list_id):
    shopping_list = ShoppingList.objects.get(pk=list_id)
    
    # Check if the current user is the owner of the list
    is_owner = request.user == shopping_list.owner
    
    if not is_owner:
        return render(request, 'shop_list/rename.html', {'not_authorized_message': 'You are not authorized to rename this list.', 'is_owner': False})
    
    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        if new_name:
            shopping_list.name = new_name
            shopping_list.save()
            messages.success(request, 'List renamed successfully!')
            return redirect('show_shopping_lists')
        else:
            messages.error(request, 'New name cannot be empty!')
    
    return render(request, 'shop_list/rename.html', {'shopping_list': shopping_list, 'is_owner': is_owner})
    
@login_required
def delete(request, list_id):
    # Get the shopping list object
    shopping_list = ShoppingList.objects.get(pk=list_id)
    
    # Check if the current user is the owner of the list
    if request.user == shopping_list.owner:
        # Delete the list
        shopping_list.delete()
        return redirect('show_shopping_lists')
    else:
        # If the user is not the owner, return a forbidden response
        return HttpResponseForbidden("You are not authorized to delete this list.")

def edit(request, list_id):
    shopping_list = ShoppingList.objects.get(pk=list_id)
    items = Item.objects.filter(shopping_list=shopping_list)

    # Check if the current user is the owner of the list
    is_owner = shopping_list.owner == request.user

    if request.method == 'POST':
        # Handle checkbox state changes
        item_ids = request.POST.getlist('item_ids')  
        for item_id in item_ids:
            item = Item.objects.get(pk=item_id)
            item.is_done = not item.is_done  # Toggle the state of the checkbox
            item.save()  # Save the changes to the database

    return render(request, 'shop_list/edit.html', {'shopping_list': shopping_list, 'items': items, 'is_owner': is_owner})


def toggle_item_done(request, item_id):
    if request.method == 'POST':
        try:
            item = Item.objects.get(pk=item_id)
            item.is_done = not item.is_done  # Toggle the "done" status
            item.save()
            return JsonResponse({'status': 'success'})
        except Item.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Item not found'}, status=404)
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'}, status=405)

'''
@login_required
def create_shopping_list(request):
    # Clear any existing messages if the user is authenticated
    if request.user.is_authenticated:
        storage = messages.get_messages(request)
        new_messages = []
        for message in storage:
            if "You have signed out." not in message.message and "Successfully signed in as" not in message.message:
                new_messages.append(message)
        # Replace the messages in the storage with the filtered messages
        request._messages._loaded_data = new_messages

    if request.method == 'POST':
        form = ShoppingListForm(request.POST)
        if form.is_valid():
            shopping_list = form.save(commit=False)
            shopping_list.owner_id = request.user.id  
            shopping_list.save()
            shopping_list_name = shopping_list.name
            messages.success(request, f'Shopping list "{shopping_list_name}" created successfully!')
            return redirect('create_shopping_list')
    else:
        form = ShoppingListForm()
    
    return render(request, 'shop_list/create_shopping_list.html', {'form': form})

def edit(request, list_id):
    shopping_list = get_object_or_404(ShoppingList, pk=list_id)
    return render(request, 'shop_list/edit.html', {'shopping_list': shopping_list})


def show_items(request, list_id):
    shopping_list = ShoppingList.objects.get(pk=list_id)
    items = Item.objects.filter(shopping_list=shopping_list)

    # Check if the current user is the owner of the list
    is_owner = shopping_list.owner == request.user

    return render(request, 'shop_list/show_items.html', {'shopping_list': shopping_list, 'items': items, 'is_owner': is_owner})





messages.success(request, 'Shopping list { } created successfully!')




@login_required
def rename(request, list_id):
    shopping_list = ShoppingList.objects.get(pk=list_id)
    
    # Check if the current user is the owner of the list
    if request.user != shopping_list.owner:
        return render(request, 'shop_list/rename.html', {'not_authorized_message': 'You are not authorized to rename this list.'})
    
    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        if new_name:
            shopping_list.name = new_name
            shopping_list.save()
            messages.success(request, 'List renamed successfully!')
            return redirect('show_shopping_lists')
        else:
            messages.error(request, 'New name cannot be empty!')
    
    return render(request, 'shop_list/rename.html', {'shopping_list': shopping_list})


def clone(request, list_id):
    original_list = ShoppingList.objects.get(pk=list_id)
    
    # Create a new ShoppingList object with the copied attributes
    cloned_list = ShoppingList.objects.create(
        name=f"{original_list.name} (Copy)",  # Update the name
        owner=original_list.owner,            # Keep the same owner
        is_private=original_list.is_private,  # Keep the same privacy status
        original_list_id=original_list.id     # Keep track of the original list ID
    )
    
    return redirect('show_shopping_lists')  # Redirect to the page showing all shopping lists










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