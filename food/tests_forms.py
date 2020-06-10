from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Brand
from .forms import BrandForm


class TestBrandForm(TestCase):
    def test_form_saves_correctly_with_valid_data(self):
        form = BrandForm({
            "name":"test_brand"
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
