from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Brand, FoodBase, FoodItem
from .forms import BrandForm, FoodBaseForm, FoodItemForm


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


class TestFoodItemForm(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="test_user",
            password="1290Pass"
        )

        self.brand = Brand.objects.create(
            name="test_brand"
        )

        self.food_base = FoodBase.objects.create(**{
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
        })

        self.food_item_data = {
            "name": "test_item",
            "description": "Test_description",
            "food": self.food_base,
            "weight": 37
        }

    def test_saves_with_expected_valid_data(self):
        form = FoodItemForm(self.food_item_data)
        self.assertTrue(form.is_valid())

        form.save()
        retrieve = FoodItem.objects.get(name="test_item")
        self.assertIsInstance(retrieve, FoodItem)
        self.assertEqual(retrieve.name, form["name"].value())
        self.assertEqual(retrieve.description, form["description"].value())
        self.assertEqual(retrieve.food.id, form["food"].value())
        self.assertIsInstance(retrieve.food, FoodBase),
        self.assertEqual(retrieve.weight, form["weight"].value())
