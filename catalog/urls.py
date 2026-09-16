from django.urls import path

from catalog.apps import CatalogConfig

from . import views

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
    path("catalog/add_product/", views.ProductCreateView.as_view(), name="add_product"),
    path(
        "catalog/product_update/<int:pk>/",
        views.ProductUpdateView.as_view(),
        name="product_update",
    ),
    path(
        "catalog/product_delete/<int:pk>/",
        views.ProductDeleteView.as_view(),
        name="product_delete",
    ),
]
