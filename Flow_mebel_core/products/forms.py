from django import forms
from django.forms import fields
from .models import Order


class OrderForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['placeholder'] = 'Your firstname'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Your lastname'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Your phone number'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control'
        self.fields['product'].widget.attrs['class'] = 'form-control'
        self.fields['material'].widget.attrs['class'] = 'form-control'
        self.fields['size'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'product', 'material', 'size']
