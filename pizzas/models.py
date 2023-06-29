from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
import os

class Topping(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="pizzas_imgs", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10.00)
    topping = models.ManyToManyField(Topping)
    
    def __str__(self):
        return self.name
   
    
Size = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large')
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, choices=Size, default='M')
    quantity = models.SmallIntegerField(default=1)
    
    def __str__(self) -> str:
        return f"Pizza {self.pizza.name} ordered by user {self.user.username}"