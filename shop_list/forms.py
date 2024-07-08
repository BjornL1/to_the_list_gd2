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

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['quantity'].widget = forms.NumberInput(attrs={'min': '1'})

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity is not None and quantity < 1:
            raise forms.ValidationError("Quantity must be at least 1")
        return quantity


class CloneForm(forms.Form):
    new_name = forms.CharField(label='New Name', max_length=100)


class DuplicateItemForm(forms.Form):
    new_name = forms.CharField(label='New Name', max_length=100)
