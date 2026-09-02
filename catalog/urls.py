from django.urls import path
from . import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.home, name="home"),
    path("contacts/", views.contacts, name="contacts"),
    path(
        "all_product_category/<int:id_category>/",
        views.category_all_product,
        name="all_product_category",
    ),
    path("contacts_success/", views.contacts, name="contacts_success"),
    path("all_category/", views.all_category, name="all_category"),
    path(
        "product_detail/<int:id_product>", views.product_detail, name="product_detail"
    ),
]
