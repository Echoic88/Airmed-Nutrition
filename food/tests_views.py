from django.test import TestCase, RequestFactory
from django.shortcuts import reverse
from .models import Brand
from .forms import BrandForm
from .views import add_brand


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


class TestAddBrandView(TestCase):
    def test_get_request_redirects_to_index(self):
        response = self.client.get(reverse("food:add_brand"))
        self.assertRedirects(response, reverse("food:index"))

    def test_post_request_saves_brand_correctly_if_valid_data(self):
        response = self.client.post(reverse("food:add_brand"), {
            "name": "test_brand"
            })
        self.assertRedirects(response, reverse("food:index"))
        self.assertIsInstance(Brand.objects.get(name="test_brand"), Brand)

    def test_post_request_does_not_save_brand_if_blank(self):
        response = self.client.post(reverse("food:add_brand"), {
            "name": ""
            })
        self.assertRedirects(response, reverse("food:index"))
        self.assertFalse(Brand.objects.filter(name="").exists())

    # def test_post_request_saves_brand_correctly_if_valid_data(self):
    #     factory = RequestFactory()
    #     request = factory.post(reverse("food:add_brand"), {
    #         "name": "test_brand"
    #     })
    #     response = add_brand(request)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertIsInstance(Brand.objects.get(name="test_brand"), Brand)
