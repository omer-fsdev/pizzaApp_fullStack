from django import forms
from .models import Order

class PizzaForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ('size', 'quantity')
        widgets = {
            'size': forms.Select(attrs={'class': 'form-select form-select-lg text-center border border-warning my-1'}),
            'quantity' : forms.NumberInput(attrs={'class': 'border border-warning text-center form-control form-control-lg my-1', 'min':'1'})
        }