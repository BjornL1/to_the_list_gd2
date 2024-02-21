from django.db import models

class ShoppingList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name