from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Brand, FoodBase, FoodItem


class BrandForm(forms.ModelForm):
    """
    Form to enter brands
    """
    class Meta:
        model = Brand
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-brandForm"
        self.helper.form_class = "blueForms"
        self.helper.form_method = "post"
        self.helper.form_action = "food:add_brand"
        self.helper.add_input(Submit("submit", "Submit"))


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-FoodBaseForm"
        self.helper.form_class = "blueForms"
        self.helper.form_method = "post"
        self.helper.form_action = "food:add_food"
        self.helper.add_input(Submit("submit", "Submit"))


class FoodItemForm(forms.ModelForm):
    """
    Form to enter details for individual food item
    """
    class Meta:
        model = FoodItem
        fields = [
            "name", "description", "food", "weight",
        ]
