# Проект my_website

## Используемые зависимости в проекте:
````
Все зависимости хранятся в файле requirements.txt

Для установки зависимостей используйте комманду в терминале:
pip install -r requirements.txt
````
## Проект использует Django framework

## Приложение 'catalog'-[catalog](catalog):
+ Контроллеры модуля-[views.py](catalog/views.py):
````
def home(requests):
    return render(requests, 'catalog/home.html')
    Возвращает домашнюю html страницу
    
def contacts(requests):
при get запросе возвращает html старницу контактов
при post запросе возвращает html страницу с сообщением об успеши отпрвки данных
````

+ URL Пути модуля - [urls.py](catalog/urls.py):
содержит url-паттерны пути обрабатываемые контроллерами [views.py](catalog/views.py)
````
urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts')
]
````

+ Папка [templates](catalog/templates):
````
Содержит html файлы такие как:
home.html
contacts.html
````