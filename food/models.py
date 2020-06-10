import uuid
from django.db import models
from django.core.validators import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.
class Brand(models.Model):
    """
    Model for food Brand names
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

    def clean(self):
        if self.name is None or self.name == "":
            raise ValidationError(
                "Name is required", code="required_field"
            )


class FoodBase(models.Model):
    """
    Store base food nutritional information. Nutrional values
    in this model containf values per 100g/100ml inline with
    EU packaging requirements.
    fat_unsaturated and carb_non_sugar fields are calculated
    using pre-save receiver rather than user entry
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(
        max_length=70, null=False, blank=False
    )
    description = models.TextField(
        max_length=200, blank=True
    )
    user = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL
    )
    brand = models.ForeignKey(
        Brand, null=True, on_delete=models.SET_NULL
    )
    energy = models.PositiveSmallIntegerField(
        null=True
    )
    fat_total = models.DecimalField(
        max_digits=4, decimal_places=2, null=True
    )
    fat_saturated = models.DecimalField(
        max_digits=4, decimal_places=2, null=True
    )
    fat_unsaturated = models.DecimalField(
        max_digits=4, decimal_places=2, null=True
    )
    carb_total = models.DecimalField(
        max_digits=4, decimal_places=2, null=True
    )
    carb_sugar = models.DecimalField(
        max_digits=4, decimal_places=2, null=True
    )
    carb_non_sugar = models.DecimalField(
        max_digits=4, decimal_places=2, null=True
    )
    fibre = models.DecimalField(
        max_digits=4, decimal_places=2, null=True
    )
    protein = models.DecimalField(
        max_digits=4, decimal_places=2, null=True
    )
    salt_amount = models.DecimalField(
        max_digits=4, decimal_places=2, null=True
    )
    tags = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} : {self.brand.name}'

    def clean(self):
        if type(self.energy) is not int:
            raise ValidationError(
                "Please enter a whole number", code="non_integer"
            )


@receiver(pre_save, sender=FoodBase)
def compare_answers(sender, instance, *args, **kwargs):
    """
    calculate fat_unsaturated and carb_non_sugars
    """
    if instance.fat_total is not None or instance.fat_total != 0:
        instance.fat_unsaturated = instance.fat_total - instance.fat_saturated

    if instance.carb_total is not None or instance.carb_total != 0:
        instance.carb_non_sugar = instance.carb_total - instance.carb_sugar
