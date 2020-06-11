from django.urls import path
from .views import index, add_brand, add_food, add_food_item

app_name = "food"
urlpatterns = [
    path("", index, name="index"),
    path("add-brand/", add_brand, name="add_brand"),
    path("add-food/", add_food, name="add_food"),
    path("add-food-item/", add_food_item, name="add_food_item")
]
