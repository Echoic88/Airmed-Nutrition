import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from food.models import FoodItem


# Create your models here.
class Meal(models.Model):
    BREAKFAST = "BR"
    LUNCH = "LN"
    DINNER = "DN"
    SUPPER = "SR"
    SNACK = "SK"
    MEAL_CHOICES = [
        (BREAKFAST, "Breakfast"),
        (LUNCH, "Lunch"),
        (DINNER, "Dinner"),
        (SUPPER, "Supper"),
        (SNACK, "Snack")
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    meal_type = models.CharField(
        max_length=2,
        choices=MEAL_CHOICES,
    )
    date = models.DateField()
    time = models.TimeField()
    template = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.meal_type} - {self.date} - {self.time}"


class MealItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food_item = models.ForeignKey(
        FoodItem, on_delete=models.SET_NULL, null=True
    )
    quantity = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.food_item.name

    def clean(self):
        if self.quantity < 0:
            raise ValidationError(
                "Quantity cannot be less than zero",
                code="negative_value"
            )
