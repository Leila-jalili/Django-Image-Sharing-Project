from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    summary = forms.CharField(label="", initial="summary", required=False,
                              widget=forms.TextInput(attrs={
                                  "placeholder": "Your summary",
                                  "class": "Your-class"}))

    class Meta:
        model = Product
        fields = ["title", "description", "price", "summary"]
