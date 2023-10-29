from django.shortcuts import render, redirect
import csv

from phones.models import Phone


def csv_reader():

    with open('phones.csv', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for c in reader:
            phone = Phone(id=c['id'],
                          name=c['name'],
                          image=c['image'],
                          price=c['price'],
                          release_date=c['release_date'],
                          lte_exists=c['lte_exists'],
                          slug=c['name'])

            phone.save()




def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = csv_reader()
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {

    }
    return render(request, template, context)
