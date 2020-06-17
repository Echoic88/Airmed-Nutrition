from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from .models import Meal, MealItem


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ["meal_type", "date", "time", "template"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-MealForm"
        self.helper.label_class = "sr-only"
        self.helper.form_method = "post"
        self.helper.form_action = "meal:add_meal"
        self.helper.add_input(Submit("submit", "Submit"))
        self.helper.layout = Layout(
            Field("meal_type"),
            Field("date"),
            Field("time"),
            Field("template"),
        )


class MealItemForm(forms.ModelForm):
    class Meta:
        model = MealItem
        fields = ["food_item", "quantity"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-MealItemForm"
        self.helper.label_class = "sr-only"
        self.helper.form_method = "post"
        self.helper.form_action = "meal:add_meal_item"
        self.helper.add_input(Submit("submit", "Submit"))
        self.helper.layout = Layout(
            Field("food_item", placeholder="Select food item:"),
            Field("quantity", placeholder="Enter quantity:"),
        )
