# Generated by Django 3.0.7 on 2020-06-16 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0002_mealitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealitem',
            name='quantity',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]