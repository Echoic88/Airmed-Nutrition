from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
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
        self.helper.label_class = "sr-only"
        self.helper.form_method = "post"
        self.helper.form_action = "food:add_brand"
        self.helper.add_input(Submit("submit", "Submit"))
        self.helper.layout = Layout(
            Field("name", placeholder="Enter brand name:")
        )


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
        help_texts = {
            "brand":"Select a brand:"
        }
        # widgets = {
        #     "brand": forms.Select(attrs={
        #         "value": "Select the brand:",
        #         "selected": True
        #     })
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-foodBaseForm"
        self.helper.label_class = "sr-only"
        self.helper.form_method = "post"
        self.helper.form_action = "food:add_food"
        self.helper.add_input(Submit("submit", "Submit"))
        self.helper.layout = Layout(
            Field("name", placeholder="Enter food name:"),
            Field("brand", value="Enter the brand:"),
            Field("energy", placeholder="Enter energy(kcal):"),
            Field("fat_total", placeholder="Enter total fat(grams):"),
            Field(
                "fat_saturated",
                placeholder="Enter saturated fat(grams):"
            ),
            Field(
                "carb_total",
                placeholder="Enter total carbohydrates(grams):"
            ),
            Field(
                "carb_sugar",
                placeholder="Enter carbohydrates - sugars(grams):"
            ),
            Field("fibre", placeholder="Enter fibre(grams):"),
            Field("protein", placeholder="Enter protein(grams):"),
            Field("salt_amount", placeholder="Enter salt(grams):"),
        )


class FoodItemForm(forms.ModelForm):
    """
    Form to enter details for individual food item
    """
    class Meta:
        model = FoodItem
        fields = [
            "name", "food", "description", "weight",
        ]
        help_texts = {
            "food":"Select a food:"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-foodItemForm"
        self.helper.label_class = "sr-only"
        self.helper.form_method = "post"
        self.helper.form_action = "food:add_food_item"
        self.helper.add_input(Submit("submit", "Submit"))
        self.helper.layout = Layout(
            Field("name", placeholder="Enter food name:"),
            Field("food"),
            Field("description", value="Enter a descripton:", rows=3),
            Field("weight", placeholder="Enter item weight (grams):"),
        )
