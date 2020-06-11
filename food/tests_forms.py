from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Brand, FoodBase
from .forms import BrandForm, FoodBaseForm


class TestBrandForm(TestCase):
    def test_form_saves_correctly_with_valid_data(self):
        form = BrandForm({
            "name": "test_brand"
        })
        form.save()

        self.assertTrue(form.is_valid())
        self.assertIsInstance(Brand.objects.get(name="test_brand"), Brand)

    def test_raise_error_if_name_too_long(self):
        test_brand = "x"*51
        form = BrandForm({
            "name": test_brand
        })

        self.assertFalse(form.is_valid())


class TestFoodBaseForm(TestCase):
    def setUp(self):

        self.brand = Brand.objects.create(
            name="test_brand"
        )

        self.form_data = {
            "name": "test_food",
            "brand": self.brand,
            "energy": 50,
            "fat_total": 3.6,
            "fat_saturated": 1.1,
            "carb_total": 2.4,
            "carb_sugar": 0.6,
            "fibre": 1.5,
            "protein": 1.5,
            "salt_amount": 1.5,
        }

    def test_form_saves_correctly_with_valid_data(self):
        form = FoodBaseForm(self.form_data)
        self.assertTrue(form.is_valid())

        form.save()
        self.assertIsInstance(FoodBase.objects.get(name="test_food"), FoodBase)

    def test_name_field_is_required(self):
        self.form_data["name"] = ""
        form = FoodBaseForm(self.form_data)

        self.assertRaises(ValidationError)
        self.assertFalse(form.is_valid())
