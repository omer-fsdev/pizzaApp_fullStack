# Generated by Django 4.2.2 on 2023-06-25 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Toppings',
            new_name='Topping',
        ),
    ]
