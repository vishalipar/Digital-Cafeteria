from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'image', 'supplier']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'price': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'quantity': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'supplier': forms.Select(attrs={'class': 'w-full p-2 border rounded-lg'}),
            'image': forms.FileInput(attrs={'class': 'w-full'}),
        }