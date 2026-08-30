from django.shortcuts import render
from catalog.models import Category, Product


def home(requests):
    category = Category.objects.all()
    products = Product.objects.all()
    contex = {"category": category[:6], "products": products[:10]}
    return render(requests, "catalog/home.html", context=contex)


def all_category(requests):
    category = Category.objects.all()
    context = {"all_category": category}
    return render(requests, "catalog/all_category.html", context=context)


def contacts(requests):
    if requests.method == "POST":
        name = requests.POST.get("name")
        phone_number = requests.POST.get("phone")
        context = {"name": name, "phone_number": phone_number}
        return render(requests, "catalog/contacts_success.html", context=context)

    return render(requests, "catalog/contacts.html")


def category_all_product(requests, id_category):
    get_products = Product.objects.filter(category_id=id_category)
    context = {"products": get_products}
    return render(requests, "catalog/all_product_category.html", context=context)
