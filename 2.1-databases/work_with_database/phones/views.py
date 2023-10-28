from django.shortcuts import render, redirect
import csv


def csv_reader():
    result = []
    with open('phones.csv', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for c in reader:
            result.append(c)
    return result


CONTENT = csv_reader()

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    context = {
        'content': CONTENT,

    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
