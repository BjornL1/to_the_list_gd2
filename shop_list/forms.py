from django import forms
from .models import ShoppingList, Item

class ShoppingListForm(forms.ModelForm):
    class Meta:
        model = ShoppingList
        fields = ['name']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'quantity']

class CloneForm(forms.Form):
    new_name = forms.CharField(label='New Name', max_length=100)

class DuplicateItemForm(forms.Form):
    new_name = forms.CharField(label='New Name', max_length=100)
