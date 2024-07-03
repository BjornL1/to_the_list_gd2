from django.db import models
from django.contrib.auth.models import User

#Model for connecting list with user
class ShoppingList(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=4)
    is_private = models.BooleanField(default=False)
    original_list_id = models.IntegerField(null=True, blank=True)
    clone_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

#Model for handling deletion of list separately for better maintainability
class ShoppingListPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    is_private = models.BooleanField(default=True)

#Model for connecting items with lists and user
class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, related_name='items')
    is_done = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  

    def __str__(self):
        return self.name

