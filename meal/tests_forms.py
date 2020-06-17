from datetime import date, time
from django.test import TestCase
from django.contrib.auth.models import User
from food.models import Brand, FoodItem, FoodBase
from .models import Meal, MealItem
from .forms import MealForm, MealItemForm


class TestMealForm(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user",
            password="1290Pass"
        )
        self.meal_data = {
            "meal_type": "DN",
            "date": date(2004, 8, 10),
            "time": time(18, 15, 3)
        }

    def test_valid_with_expected_valid_data(self):
        meal_form = MealForm(self.meal_data)
        self.assertTrue(meal_form.is_valid())

        m = meal_form.save(commit=False)
        m.user = self.user
        m.save()

        retrieve = Meal.objects.get(id=m.id)

        self.assertIsInstance(retrieve, Meal)
        self.assertEqual(retrieve.meal_type, self.meal_data["meal_type"])
        self.assertEqual(retrieve.date, self.meal_data["date"])
        self.assertEqual(retrieve.time, self.meal_data["time"])
        self.assertFalse(retrieve.template)

    def test_template_saves_as_true_if_selected(self):
        self.meal_data["template"] = True
        meal_form = MealForm(self.meal_data)

        m = meal_form.save(commit=False)
        m.user = self.user
        m.save()

        retrieve = Meal.objects.get(id=m.id)
        self.assertTrue(retrieve.template)

    def test_form_is_invalid_if_meal_type_missing(self):
        self.meal_data.pop("meal_type")
        meal_form = MealForm(self.meal_data)
        self.assertFalse(meal_form.is_valid())

    def test_form_is_invalid_if_date_missing(self):
        self.meal_data.pop("date")
        meal_form = MealForm(self.meal_data)
        self.assertFalse(meal_form.is_valid())

    def test_form_is_invalid_if_time_missing(self):
        self.meal_data.pop("time")
        meal_form = MealForm(self.meal_data)
        self.assertFalse(meal_form.is_valid())


class TestMealItemForm(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
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

        self.food_item = FoodItem.objects.create(**{
            "name": "test_item",
            "description": "test_description",
            "food": self.food_base,
            "weight": 37
        })

        self.meal = Meal.objects.create(**{
            "user": self.user,
            "meal_type": "DN",
            "date": date(2004, 8, 10),
            "time": time(18, 15, 3)
        })

        self.meal_item_data = {
            "food_item": self.food_item,
            "quantity": 2,
        }

    def test_saves_with_expected_valid_data(self):
        meal_item_form = MealItemForm(self.meal_item_data)

        self.assertTrue(meal_item_form.is_valid())

        m = meal_item_form.save(commit=False)
        m.meal = self.meal
        m.save()

        retrieve = MealItem.objects.get(id=m.id)

        self.assertIsInstance(retrieve, MealItem)
        self.assertEqual(retrieve.meal, self.meal)
        self.assertEqual(retrieve.food_item, self.food_item)
        self.assertEqual(retrieve.quantity, self.meal_item_data["quantity"])

    def test_form_is_invalid_if_no_food_item(self):
        self.meal_item_data.pop("food_item")
        meal_item_form = MealItemForm(self.meal_item_data)

        self.assertFalse(meal_item_form.is_valid())

