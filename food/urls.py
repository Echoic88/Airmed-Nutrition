from django.urls import path
from .views import index, add_brand

app_name = "food"
urlpatterns = [
    path("", index, name="index"),
    path("add-brand/", add_brand, name="add_brand"),
]
