from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView

from catalog.forms import FormContact
from catalog.models import Category, Product


class HomeListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"


class CategoryListView(ListView):
    model = Category
    template_name = "catalog/all_category.html"
    context_object_name = "all_category"


class ContactFormView(FormView):
    form_class = FormContact
    template_name = "catalog/contacts.html"
    success_url = reverse_lazy("catalog:home")


class AllCategoryProduct(ListView):
    model = Product
    template_name = "catalog/all_product_category.html"
    context_object_name = "products"

    def get_queryset(self):
        content = super().get_queryset()
        category_id = self.kwargs.get("pk")
        return content.filter(category_id=category_id)


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product_detail"
