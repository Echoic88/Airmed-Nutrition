from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BrandForm, FoodBaseForm, FoodItemForm


# Create your views here.
def index(request):
    """
    Display index page for food app
    """
    brand_form = BrandForm()
    food_base_form = FoodBaseForm()
    food_item_form = FoodItemForm()
    return render(request, "food/index.html", {
        "brand_form": brand_form,
        "food_base_form": food_base_form,
        "food_item_form": food_item_form,
    })


def add_brand(request):
    """
    view for form to add brand to Brand model
    """
    if request.method == "POST":
        brand_form = BrandForm(request.POST)
        if brand_form.is_valid():
            brand_form.save()
            messages.info(request, "Brand saved successfully")
            return redirect(reverse("food:index"))
        else:
            messages.error(request, "Error - brand not saved")
            return redirect(reverse("food:index"))
    else:
        return redirect(reverse("food:index"))


@login_required
def add_food(request):
    """
    view for form to add food to FoodBase model
    """
    if request.method == "POST":
        food_base_form = FoodBaseForm(request.POST)
        if food_base_form.is_valid():
            f = food_base_form.save(commit=False)
            f.user = request.user
            f.save()
            messages.info(request, "Food saved successfully")
            return redirect(reverse("food:index"))
        else:
            messages.error(request, "Error - food not saved")
            return redirect(reverse("food:index"))
    else:
        return redirect(reverse("food:index"))


def add_food_item(request):
    """
    view for form to add food to FoodBase model
    """
    if request.method == "POST":
        food_base_form = FoodItemForm(request.POST)
        if food_base_form.is_valid():
            food_base_form.save(commit=False)
            messages.info(request, "Food item saved successfully")
            return redirect(reverse("food:index"))
        else:
            messages.error(request, "Error - food item not saved")
            return redirect(reverse("food:index"))
    else:
        return redirect(reverse("food:index"))
