from django.shortcuts import render
from django.http import HttpResponse


def home(requests):
    return render(requests, 'catalog/home.html')


def contacts(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        message = requests.POST.get('message')
        phone_number = requests.POST.get('phone')
        html_content = f"""
        <html>
        <body>
        <div style='background-color : black; text-align : center'>
            <h1 style='color : white'>Успешно отправлено!</h1>
        </div>
        <div style='text-align : center'>
            <p>Дорогой {name} Ваше сообщение успешно получено</p>
            <p>Свяжемся с вами по номеру {phone_number}</p>
            <a href='http://127.0.0.1:8000/'>На главную</a>
        </div>
        </body>
        </html>
        """

        return HttpResponse(html_content)

    return render(requests, 'catalog/contacts.html')
