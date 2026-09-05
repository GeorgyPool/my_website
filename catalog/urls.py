from django.urls import path
from . import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("catalog/home/", views.HomeListView.as_view(), name="home"),
    path("catalog/contacts/", views.ContactFormView.as_view(), name="contacts"),
    path(
        "catalog/all_product_category/<int:pk>/",
        views.AllCategoryProduct.as_view(),
        name="all_product_category",
    ),
    path(
        "catalog/all_category/", views.CategoryListView.as_view(), name="all_category"
    ),
    path(
        "catalog/product_detail/<int:pk>/",
        views.ProductDetailView.as_view(),
        name="product_detail",
    ),
]
