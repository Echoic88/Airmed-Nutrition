from django.test import TestCase
from django.shortcuts import reverse


class TestIndex(TestCase):
    def test_index_view_diplays_correct_template(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("food/index.html")

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse("food:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("food/index.html")
