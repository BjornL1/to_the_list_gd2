# Generated by Django 4.2.10 on 2024-03-04 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_list', '0008_shoppinglist_clone_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
