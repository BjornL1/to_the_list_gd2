from django.db import models
from django.contrib.auth.models import User

class ShoppingList(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=4)
    is_private = models.BooleanField(default=False)
    original_list_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
        
class ShoppingListPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=True)

class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

'''
from django.db import models

class ShoppingList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
'''