from datetime import datetime
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from food.models import Brand, FoodBase, FoodItem
from .models import Meal, MealItem


# helper function to return time as string without microseconds
def time_string(time):
    return time.strftime("%Y, %m, %d %H:%M:%S")


# Create your tests here.
class TestMealModel(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="test_user",
            password="1290Pass"
        )

        self.meal_data = {
            "user": self.user,
            "meal_type": "DN",
            "date_time": datetime(2004, 8, 10, 18, 15, 00),
        }

    def test_saves_with_expected_valid_data(self):
        meal = Meal.objects.create(**self.meal_data)
        retrieve = Meal.objects.get(id=meal.id)

        self.assertIsInstance(retrieve, Meal)
        self.assertEqual(retrieve.user, self.user)
        self.assertIsInstance(retrieve.user, User)
        self.assertEqual(retrieve.meal_type, self.meal_data["meal_type"])
        self.assertEqual(
            time_string(retrieve.date_time),
            time_string(self.meal_data["date_time"])
        )
        self.assertFalse(retrieve.template)

    def test_raise_validation_error_if_no_user(self):
        self.meal_data.pop("user")
        meal = Meal(**self.meal_data)

        with self.assertRaises(ValidationError):
            meal.full_clean()

    def test_only_allowed_values_for_meal_type_options(self):
        self.meal_data["meal_type"] = "NV"
        meal = Meal(**self.meal_data)

        with self.assertRaises(ValidationError):
            meal.full_clean()


class TestMealItemModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user",
            password="1290Pass"
        )

        self.meal = Meal.objects.create(**{
            "user": self.user,
            "meal_type": "DN",
            "date_time": datetime(2004, 8, 10, 18, 15, 00),
        })

        self.brand = Brand.objects.create(**{
            "name": "test_brand"
        })

        self.food = FoodBase.objects.create(**{
            "name": "test_food",
            "user": self.user,
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
            "name": "test_food_item",
            "description": "test_description",
            "food": self.food,
            "weight": 37.5,
        })

        self.meal_item_data = {
            "meal": self.meal,
            "food_item": self.food_item,
            "quantity": 2
        }

    def test_MealItem_saves_with_expected_valid_data(self):
        MealItem.objects.create(**self.meal_item_data)
        retrieve = MealItem.objects.get(food_item__name="test_food_item")

        self.assertIsInstance(retrieve, MealItem)

    def test_negative_quantity_raises_validation_error(self):
        self.meal_item_data["quantity"] = -1
        meal_item = MealItem(**self.meal_item_data)

        with self.assertRaises(ValidationError):
            meal_item.full_clean()
