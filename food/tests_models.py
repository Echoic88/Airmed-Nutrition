from django.test import TestCase
from .models import Brand


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
