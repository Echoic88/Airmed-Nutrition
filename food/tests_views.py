from django.test import TestCase, RequestFactory
from django.shortcuts import reverse
from django.contrib.auth.models import User
from .models import Brand, FoodBase
from .forms import BrandForm, FoodBaseForm, FoodItemForm
from .views import add_brand, add_food


class TestIndexView(TestCase):
    def test_index_view_diplays_correct_template(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("food/index.html")

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse("food:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("food/index.html")

    def test_context_contains_correct_forms(self):
        response = self.client.get(reverse("food:index"))
        self.assertIsInstance(response.context["brand_form"], BrandForm)
        self.assertIsInstance(response.context["food_base_form"], FoodBaseForm)
        self.assertIsInstance(response.context["food_item_form"], FoodItemForm)



class TestAddBrandView(TestCase):
    def test_get_request_redirects_to_index(self):
        response = self.client.get(reverse("food:add_brand"))
        self.assertRedirects(response, reverse("food:index"))

    def test_post_request_saves_brand_correctly_if_valid_data(self):
        response = self.client.post(reverse("food:add_brand"), {
            "name": "test_brand"
            })
        self.assertRedirects(response, reverse("food:index"))
        self.assertTrue(Brand.objects.filter(name="test_brand").exists())

    def test_post_request_does_not_save_brand_if_blank(self):
        response = self.client.post(reverse("food:add_brand"), {
            "name": ""
            })
        self.assertRedirects(response, reverse("food:index"))
        self.assertFalse(Brand.objects.filter(name="").exists())


# class TestAddFoodView(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(
#             username="test_user",
#             password="1290Pass"
#         )
#         self.brand = Brand.objects.create(
#             name="test_brand"
#         )
#         self.food_data = {
#             "name": "test_food",
#             "brand": self.brand,
#             "energy": 50,
#             "fat_total": 3.6,
#             "fat_saturated": 1.1,
#             "carb_total": 2.4,
#             "carb_sugar": 0.6,
#             "fibre": 1.5,
#             "protein": 1.5,
#             "salt_amount": 1.5,
#         }

#     def test_get_request_redirects_to_index(self):
#         response = self.client.get(reverse("food:add_food"))
#         self.assertRedirects(response, reverse("food:index"))

#     def test_post_request_saves_food_base_correctly_if_valid_data(self):
#         response = self.client.post(reverse("food:add_food"), self.food_data)
#         self.assertRedirects(response, reverse("food:index"))
#         self.assertTrue(FoodBase.objects.get(name="test_food").exists())
