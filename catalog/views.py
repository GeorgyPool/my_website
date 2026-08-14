from django.shortcuts import render


def home(requests):
    return render(requests, 'catalog/home.html')


def contacts(requests):
    return render(requests, 'catalog/contacts.html')
