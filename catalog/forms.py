from django import forms


class FormContact(forms.Form):
    name = forms.CharField(max_length=100, label="Имя", help_text="Иван Иванов")
    phone = forms.CharField(
        max_length="20", label="Номер телефона", help_text="9-999-99-99-99"
    )
    message = forms.CharField(
        widget=forms.Textarea, label="Сообщение", help_text="Сообщение"
    )
