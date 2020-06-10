from django.test import TestCase
from django.core.validators import ValidationError
from django.contrib.auth.models import User
from .models import Brand, FoodBase, FoodItem


# Helper function
def round_6(number):
    """
    Round values in tests below to 6 decimal places to mitigate
    against float discrepancies in comparisons while still
    at an acceptable decimal resolution
    """
    return round(number, 6)


# Create your tests here.
class TestBrandModel(TestCase):
    """
    Tests for the Brand model
    """
    def test_valid_with_expected_valid_data(self):
        test = Brand.objects.create(
            name="test_brand",
        )

        retrieve = Brand.objects.get(name="test_brand")
        self.assertIsInstance(retrieve, Brand)
        self.assertEqual(retrieve.name, test.name)

    def test_brand_is_required(self):
        test = Brand(name="")
        with self.assertRaises(ValidationError):
            test.clean()


class TestFoodBaseModel(TestCase):
    """
    Tests FoodBase model
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user",
            password="1290Pass"
        )

        self.brand = Brand.objects.create(name="test_brand")

        self.food_data = {
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
        }

    def test_saves_with_expected_valid_data(self):
        """
        test all fields except tags
        """
        FoodBase.objects.create(**self.food_data)
        retrieve = FoodBase.objects.get(name="test_food")
        self.assertIsInstance(retrieve, FoodBase)
        self.assertEqual(retrieve.name, self.food_data["name"])
        self.assertEqual(retrieve.user, self.food_data["user"])
        self.assertIsInstance(retrieve.user, User)
        self.assertEqual(retrieve.brand, self.food_data["brand"])
        self.assertIsInstance(retrieve.brand, Brand)
        self.assertEqual(retrieve.energy, self.food_data["energy"])
        self.assertEqual(
            float(retrieve.fat_total), self.food_data["fat_total"]
        )
        self.assertEqual(
            float(retrieve.fat_saturated), self.food_data["fat_saturated"]
        )
        self.assertEqual(
            float(retrieve.carb_total), self.food_data["carb_total"]
        )
        self.assertEqual(
            float(retrieve.carb_sugar), self.food_data["carb_sugar"]
        )
        self.assertEqual(
            float(retrieve.fibre), self.food_data["fibre"]
        )
        self.assertEqual(
            float(retrieve.protein), self.food_data["protein"]
        )
        self.assertEqual(
            float(retrieve.salt_amount), self.food_data["salt_amount"]
        )

    def test_calculated_fields_are_saved_correctly(self):
        """
        fat_unsaturated and carb_non_sugars are calculated
        using pre-save receiver
        """
        food = FoodBase.objects.create(**self.food_data)

        self.assertEqual(
            food.fat_unsaturated, food.fat_total-food.fat_saturated
        )
        self.assertEqual(
            food.carb_non_sugar, food.carb_total-food.carb_sugar
        )


class TestFoodItem(TestCase):
    """
    Tests for the FoodItem model
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user",
            password="1290Pass"
        )

        self.brand = Brand.objects.create(name="test_brand")

        self.food_data = {
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
        }
        self.food = FoodBase.objects.create(**self.food_data)

        self.food_item_data = {
            "name": "test_item",
            "description": "test_description",
            "food": self.food,
            "weight": 37.5,
        }

    def test_saves_with_expected_valid_data(self):
        test_item = FoodItem.objects.create(**self.food_item_data)
        retrieve = FoodItem.objects.get(name="test_item")

        self.assertIsInstance(retrieve, FoodItem)
        self.assertEqual(retrieve.name, test_item.name)
        self.assertEqual(retrieve.description, test_item.description)
        self.assertEqual(retrieve.food.name, test_item.food.name)
        self.assertIsInstance(retrieve.food, FoodBase)
        self.assertEqual(retrieve.weight, test_item.weight)

    def test_calculate_nutrients_per_item(self):
        test_item = FoodItem.objects.create(**self.food_item_data)

        self.assertEqual(
            test_item.energy,
            round_6(
                self.food_data["energy"] / 100 * self.food_item_data["weight"]
            )
        )
        self.assertEqual(
            test_item.fat_total,
            round_6(
                self.food_data["fat_total"]
                / 100
                * self.food_item_data["weight"]
            )
        )
        self.assertEqual(
            test_item.fat_saturated,
            round_6(
                self.food_data["fat_saturated"]
                / 100
                * self.food_item_data["weight"]
            )
        )
        self.assertEqual(
            test_item.fat_unsaturated,
            round_6(
                (self.food_data["fat_total"] - self.food_data["fat_saturated"])
                / 100
                * self.food_item_data["weight"]
            )
        )
        self.assertEqual(
            test_item.carb_total,
            round_6(
                self.food_data["carb_total"]
                / 100
                * self.food_item_data["weight"]
            )
        )
        self.assertEqual(
            test_item.carb_sugar,
            round_6(
                self.food_data["carb_sugar"]
                / 100
                * self.food_item_data["weight"]
            )
        )
        self.assertEqual(
            test_item.carb_non_sugar,
            round_6(
                (self.food_data["carb_total"] - self.food_data["carb_sugar"])
                / 100
                * self.food_item_data["weight"]
            )
        )
        self.assertEqual(
            test_item.fibre,
            round_6(
                self.food_data["fibre"] / 100 * self.food_item_data["weight"]
            )
        )
        self.assertEqual(
            test_item.protein,
            round_6(
                self.food_data["protein"] / 100 * self.food_item_data["weight"]
            )
        )
        self.assertEqual(
            test_item.salt_amount,
            round_6(
                self.food_data["salt_amount"]
                / 100
                * self.food_item_data["weight"]
            )
        )
