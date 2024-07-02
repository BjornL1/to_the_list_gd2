from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ShoppingListForm, ItemForm
from .models import ShoppingList, Item, ShoppingListPreference
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseForbidden
from django.http import HttpResponseNotFound
from django.utils.text import slugify
from .forms import CloneForm, DuplicateItemForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return render(request, 'shop_list/index.html')


@login_required
def create_shopping_list(request):
    # Clear any existing messages if the user is authenticated
    if request.user.is_authenticated:
        storage = messages.get_messages(request)
        new_messages = []
        for message in storage:
            if "You have signed out." not in message.message and \
               "Successfully signed in as" not in message.message:
                new_messages.append(message)
        # Replace the messages in the storage with the filtered messages
        request._messages._loaded_data = new_messages

    if 'form_page_visited' in request.session:
        del request.session['form_page_visited']

    if request.method == 'POST':
        form = ShoppingListForm(request.POST)
        if form.is_valid():
            shopping_list_name = form.cleaned_data['name']

            # Check if a shopping list with the same name already exists
            if ShoppingList.objects.filter(name=shopping_list_name).exists():
                error_message = f'A shopping list with the name "{shopping_list_name}" already exists. Please use another name.'
                messages.error(request, f'A shopping list with the name "{shopping_list_name}" already exists. Please use another name.')
                return render(request, 'shop_list/create_shopping_list.html', {'form': form, 'error_message': error_message})
            else:
                shopping_list = form.save(commit=False)
                shopping_list.owner_id = request.user.id
                shopping_list.save()

                messages.success(request, f'Shopping list "{shopping_list_name}" created successfully!')
                return redirect('add_item', list_id=shopping_list.id)

    else:
        form = ShoppingListForm()

    return render(request, 'shop_list/create_shopping_list.html', {'form': form})


@login_required
def show_shopping_lists(request):
    # Fetch current user's lists
    my_lists = ShoppingList.objects.filter(owner=request.user).order_by('-id')
    
    # Fetch other public lists excluding the current user's lists
    other_lists = ShoppingList.objects.filter(is_private=False).exclude(owner=request.user).order_by('-id')

    # Paginate my lists and other lists with 10 items per page
    paginator_my_lists = Paginator(my_lists, 5)
    paginator_other_lists = Paginator(other_lists, 5)

    # Get the current page numbers from the request
    page_number_my_lists = request.GET.get('page_my_lists')
    page_number_other_lists = request.GET.get('page_other_lists')

    # Get the paginated objects
    my_lists_page_obj = paginator_my_lists.get_page(page_number_my_lists)
    other_lists_page_obj = paginator_other_lists.get_page(page_number_other_lists)

    # Prepare the lists with usernames and done counts for display
    def get_list_data(page_obj):
        lists_with_usernames = []
        for shopping_list in page_obj:
            done_count = shopping_list.items.filter(is_done=True).count()
            lists_with_usernames.append((shopping_list, shopping_list.owner.username, done_count))
        return lists_with_usernames

    my_lists_with_usernames = get_list_data(my_lists_page_obj)
    other_lists_with_usernames = get_list_data(other_lists_page_obj)

    # Get the logged-in user
    logged_in_user = request.user

    # Render the template with the context
    return render(request, 'shop_list/show_shopping_lists.html', {
        'my_lists_with_usernames': my_lists_with_usernames,
        'other_lists_with_usernames': other_lists_with_usernames,
        'my_lists_page_obj': my_lists_page_obj,
        'other_lists_page_obj': other_lists_page_obj,
        'logged_in_user': logged_in_user,
    })


@login_required
def add_item(request, list_id):
    # Fetch the shopping list
    shopping_list = get_object_or_404(ShoppingList, pk=list_id)

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.shopping_list = shopping_list

            # Set the created_by field to the current user
            item.created_by = request.user
            print("Item created by:", item.created_by)
            item.save()
            return redirect('show_items', list_id=list_id)
    else:
        form = ItemForm()

    return render(request, 'shop_list/add_item.html', {
        'form': form,
        'shopping_list': shopping_list
    })


@login_required
def show_items(request, list_id):
    # Retrieve the shopping list object
    shopping_list = get_object_or_404(ShoppingList, pk=list_id)

    # Retrieve all items associated with the shopping list
    all_items = shopping_list.items.order_by('id')

    # Enumerate the items
    enumerated_items = [
        (index + 1, item) for index, item in enumerate(all_items)
    ]

    context = {
        'shopping_list': shopping_list,
        'enumerated_items': enumerated_items,
        'logged_in_user': request.user,
        'all_items': all_items,  # Include all_items in the context
    }

    return render(request, 'shop_list/show_items.html', context)


@login_required
def toggle_list_status(request, list_id):
    if request.method == 'POST':
        try:
            shopping_list = get_object_or_404(ShoppingList, pk=list_id)
            # Check if the user has a preference for the list's privacy status
            user_preference = ShoppingListPreference.objects.filter(
                user=request.user,
                shopping_list=shopping_list
            ).first()
            if user_preference:
                # Use the user's preference if available
                shopping_list.is_private = user_preference.is_private
            else:
                # Otherwise, toggle the privacy status as before
                shopping_list.is_private = not shopping_list.is_private
            shopping_list.save()
            return JsonResponse({'status': 'success',
                                 'is_public': not shopping_list.is_private})
        except ShoppingList.DoesNotExist:
            return JsonResponse({'status': 'error',
                                 'message': 'Shopping list not found'},
                                status=404)
    else:
        return JsonResponse({'status': 'error',
                             'message': 'Only POST requests are allowed'},
                            status=405)


@login_required
def clone(request, list_id):
    original_list = get_object_or_404(ShoppingList, pk=list_id)

    if request.method == 'POST':
        form = CloneForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['new_name']

            # Check if a list with the same name already exists
            base_name = new_name
            suffix = 1
            while ShoppingList.objects.filter(name=new_name).exists():
                new_name = f"{base_name} Copy {suffix}"
                suffix += 1

            # Clone the shopping list
            cloned_list = ShoppingList.objects.create(
                name=new_name,
                owner=request.user,
                is_private=original_list.is_private
            )

            original_list.clone_count += 1
            original_list.save()

            for item in original_list.items.all():
                cloned_item = Item.objects.create(
                    name=item.name,
                    quantity=item.quantity,
                    shopping_list=cloned_list,
                    created_by=request.user
                )

            # Render the clone confirmation template
            return render(
                request,
                'shop_list/clone_confirmation.html',
                {'shopping_list': original_list, 'new_name': new_name}
            )
    else:
        form = CloneForm()

    return render(request, 'shop_list/clone.html',
                  {'form': form, 'shopping_list': original_list})


@login_required
def duplicate_item(request, item_id):
    original_item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        form = DuplicateItemForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['new_name']

            # Check if an item with the same name already exists
            base_name = new_name
            suffix = 1
            while Item.objects.filter(name=new_name).exists():
                new_name = f"{base_name} Copy {suffix}"
                suffix += 1

            # Duplicate the item
            duplicated_item = Item.objects.create(
                name=new_name,
                quantity=original_item.quantity,
                shopping_list=original_item.shopping_list,  # Associate the
                # duplicated item with the same shopping list
                created_by=request.user
            )

            # Render the duplicate confirmation template
            return render(
                request,
                'shop_list/duplicate_item_confirmation.html',
                {
                    'item': original_item,
                    'new_name': new_name
                }
            )
    else:
        form = DuplicateItemForm()

    return render(request, 'shop_list/duplicate_item.html', {
        'form': form,
        'item': original_item
    })


@login_required
def rename(request, list_id):
    shopping_list = get_object_or_404(ShoppingList, pk=list_id)

    # Check if the current user is the owner of the list
    is_owner = request.user == shopping_list.owner

    if not is_owner:
        return render(
            request,
            'shop_list/rename.html',
            {
                'not_authorized_message': 'You are unauthorized for the list.',
                'is_owner': False
            }
        )

    old_name = shopping_list.name  # Get the old name before updating

    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        if new_name:
            shopping_list.name = new_name
            shopping_list.save()
            return render(request, 'shop_list/rename_confirmation.html', {
                'old_name': old_name,
                'new_name': new_name
            })
        else:
            messages.error(request, 'New name cannot be empty!')

    return render(request, 'shop_list/rename.html', {
        'shopping_list': shopping_list,
        'is_owner': is_owner
    })


@login_required
def item_rename(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    shopping_list = item.shopping_list

    # Check if the current user is the owner of the item
    is_owner = request.user == shopping_list.owner
    is_creator = request.user == item.created_by

    if not is_owner and not is_creator:
        return render(
            request,
            'shop_list/item_rename.html',
            {
                'not_authorized_message': 'You are unauthorized for the item.',
                'is_owner': False
            }
        )

    old_name = item.name  # Get the old item name before updating

    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        if new_name:
            item.name = new_name
            item.save()
            return render(request, 'shop_list/item_rename_confirmation.html', {
                'old_name': old_name,
                'new_name': new_name
            })
        else:
            messages.error(request, 'New name cannot be empty!')

    return render(request, 'shop_list/item_rename.html', {
        'item': item,
        'is_owner': is_owner,
        'old_name': old_name
    })


@login_required
def delete(request, list_id):
    try:
        shopping_list = ShoppingList.objects.get(pk=list_id)

        # Check if the current user is the owner of the list
        if request.user != shopping_list.owner:
            return HttpResponseForbidden(
                "You are not authorized to delete this list."
            )

        # If the request method is POST, it means the user
        # has confirmed the deletion
        if request.method == 'POST':
            # Delete the list
            shopping_list.delete()
            # Render the deletion confirmation template
            return render(request, 'shop_list/delete_confirmation.html', {
               'shopping_list': shopping_list
            })

        # If the request method is GET, it means the user is
        # viewing the confirmation page
        else:
            # Redirect to the confirmation page
            return redirect('delete_confirmation', list_id=list_id)

    except ShoppingList.DoesNotExist:
        # If the shopping list does not exist, return a 404 response
        return HttpResponseNotFound("Shopping List not found.")


@login_required
def delete_item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)

        # Check if the current user is the owner of the item's shopping list
        if request.user != item.shopping_list.owner:
            return HttpResponseForbidden(
                "You are not authorized to delete this item.")

        # If the request method is POST, it means the user
        # has confirmed the deletion
        if request.method == 'POST':
            # Delete the item
            item.delete()
            # Render the deletion confirmation template
            return render(
                request,
                'shop_list/delete_item_confirmation.html',
                {'item': item}
            )

        # If the request method is GET, it means the user is viewing
        # # the confirmation page
        else:
            # Redirect to the confirmation page
            return redirect('delete_item_confirmation', item_id=item_id)

    except Item.DoesNotExist:
        # If the item does not exist, return a 404 response
        return HttpResponseNotFound("Item not found.")


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

    return render(
        request,
        'shop_list/edit.html',
        {'shopping_list': shopping_list, 'items': items, 'is_owner': is_owner}
    )


def toggle_item_done(request, item_id):
    if request.method == 'POST':
        try:
            item = Item.objects.get(pk=item_id)
            item.is_done = not item.is_done  # Toggle the "done" status
            item.save()
            return JsonResponse({'status': 'success'})
        except Item.DoesNotExist:
            return JsonResponse(
                {'status': 'error', 'message': 'Item not found'},
                status=404
            )
    else:
        return JsonResponse(
            {'status': 'error', 'message': 'Only POST requests are allowed'},
            status=405
        )


def edit_item(request, item_id):
    # Retrieve the item object
    item = get_object_or_404(Item, pk=item_id)
    shopping_list = item.shopping_list

    context = {
        'item': item,
        'shopping_list': shopping_list,
    }

    return render(request, 'shop_list/edit_item.html', context)


def index(request):
    if request.user.is_authenticated:
        return redirect('show_shopping_lists')
    else:
        # Render the default home page template for non-authenticated users
        return render(request, 'shop_list/index.html')


def learn_view(request):
    return render(request, 'learn.html')
