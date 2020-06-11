from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import BrandForm


# Create your views here.
def index(request):
    """
    Display index page for food app
    """
    brand_form = BrandForm()
    return render(request, "food/index.html", {
        "brand_form": brand_form,
    })


def add_brand(request):
    """
    form to add brand
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
        brand_form = BrandForm()
    return redirect(reverse("food:index"))
