from django import forms
from .models import Brand, FoodBase, FoodItem


class BrandForm(forms.ModelForm):
    """
    Form to enter brands
    """
    class Meta:
        model = Brand
        fields = ["name"]


class FoodBaseForm(forms.ModelForm):
    """
    Form for entering base food details
    """
    class Meta:
        model = FoodBase
        fields = [
            "name", "brand", "energy", "fat_total", "fat_saturated",
            "carb_total", "carb_sugar", "fibre", "protein", "salt_amount",
        ]
