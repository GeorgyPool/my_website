from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product

DANGER_WORDS = [
    "казино",
    "биржа",
    "обман",
    "криптовалюта",
    "дешево",
    "полиция",
    "крипта",
    "бесплатно",
    "радар",
]


class FormContact(forms.Form):
    name = forms.CharField(max_length=100, label="Имя", help_text="Иван Иванов")
    phone = forms.CharField(max_length="20", label="Номер телефона")
    message = forms.CharField(
        widget=forms.Textarea, label="Сообщение", help_text="Сообщение"
    )

    def __init__(self, *args, **kwargs):
        super(FormContact, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update({"class": "form-control"})

        self.fields["phone"].widget.attrs.update(
            {"class": "form-control", "placeholder": "9-999-99-99-99"}
        )

        self.fields["message"].widget.attrs.update({"class": "form-control"})


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name_product"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите имя продукта"}
        )

        self.fields["descriptions"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание"}
        )

        self.fields["image"].widget.attrs.update({"class": "form-control"})

        self.fields["category"].widget.attrs.update({"class": "form-control"})

        self.fields["purchase_price"].widget.attrs.update({"class": "form-control"})

    def clean_purchase_price(self):
        purchase_price = self.cleaned_data.get("purchase_price")
        if purchase_price <= 0:
            raise ValidationError("Сума не может быть меньше или равна нулю")
        return purchase_price

    def clean_name_product(self):
        name_product = self.cleaned_data.get("name_product").title()
        search_product = Product.objects.filter(name_product=name_product)

        if self.instance.pk:
            search_product = search_product.exclude(pk=self.instance.pk)

        if search_product.exists():
            raise ValidationError("Товар с таким именем уже существует")

        return name_product.title()

    def clean(self):
        clean_data = super().clean()
        name_product_raw = clean_data.get("name_product")
        descriptions_raw = clean_data.get("descriptions")

        name_product = (
            name_product_raw.lower() if name_product_raw is not None else None
        )
        descriptions = (
            descriptions_raw.lower() if descriptions_raw is not None else None
        )

        list_string = [x for x in [name_product, descriptions] if x is not None]
        if list_string:
            string = " ".join(list_string).lower()
        else:
            string = ""

        if string:
            for words in DANGER_WORDS:
                if words.lower() in string:
                    raise ValidationError(f"Найдено запрещенное слово: {words}")
