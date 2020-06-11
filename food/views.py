from django.shortcuts import render


# Create your views here.
def index(request):
    """
    Display index page for food app
    """
    return render(request, "food/index.html")


def add_brand(request):
    """
    form to add brand
    """
    pass
