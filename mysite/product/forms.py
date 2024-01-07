from django import forms

from product.models import Product, Category


class BuyProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("First message")
        
