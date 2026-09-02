from django.shortcuts import render, get_object_or_404
from catalog.models import Category, Product


def home(requests):
    content = Product.objects.all()
    context = {"products": content}
    return render(requests, "catalog/home.html", context=context)


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


def product_detail(requests, id_product):
    content = get_object_or_404(Product, id=id_product)
    context = {"product_detail": content}
    return render(requests, "catalog/product_detail.html", context=context)
