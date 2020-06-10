from django import forms
from .models import Brand


class BrandForm(forms.ModelForm):
    """
    Form to enter brands
    """
    class Meta:
        model = Brand
        fields = ["name"]
