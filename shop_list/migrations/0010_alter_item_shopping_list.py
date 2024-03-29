# Generated by Django 4.2.10 on 2024-03-13 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_list', '0009_item_is_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='shopping_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shop_list.shoppinglist'),
        ),
    ]
