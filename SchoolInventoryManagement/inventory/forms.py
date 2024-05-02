from django import forms

class CartAddItemForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)

class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(max_length=100)
    