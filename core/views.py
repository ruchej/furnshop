from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')


def products(request):
    return render(request, 'core/products.html')


def contact(request):
    return render(request, 'core/contact.html')
