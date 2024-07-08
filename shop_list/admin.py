from django.contrib import admin
from .models import ShoppingList, ShoppingListPreference, Item

# Register your models here.
admin.site.register(ShoppingList)
admin.site.register(ShoppingListPreference)
admin.site.register(Item)