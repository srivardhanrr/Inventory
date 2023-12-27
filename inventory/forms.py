from django import forms
from .models import Stock


class StockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):  # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['image'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['description'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['quantity_sqft'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['quantity_pcs'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})

    class Meta:
        model = Stock
        fields = ['name', 'quantity_sqft', 'quantity_pcs', 'image', 'description']
