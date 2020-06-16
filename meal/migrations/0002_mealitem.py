# Generated by Django 3.0.7 on 2020-06-16 14:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_auto_20200616_1508'),
        ('meal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('food_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food.FoodItem')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meal.Meal')),
            ],
        ),
    ]