from django.shortcuts import render, redirect
import csv
from django.shortcuts import render, get_object_or_404
from phones.models import Phone


# def csv_reader():
#     with open('phones.csv', newline='', encoding='utf-8') as file:
#         reader = csv.DictReader(file, delimiter=';')
#         for c in reader:
#             phone = Phone(id=c['id'],
#                           name=c['name'],
#                           image=c['image'],
#                           price=c['price'],
#                           release_date=c['release_date'],
#                           lte_exists=c['lte_exists'],
#                           )
#
#             phone.save()


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    template = 'catalog.html'
    phones = Phone.objects.all()
    phone = []
    if sort == 'name':
        for v in list(sorted(phones, key=lambda x: x.name)):
            phone.append(v)

    elif sort == 'min_price':
        for v in list(sorted(phones, key=lambda x: x.price)):
            phone.append(v)
    elif sort == 'max_price':
        for v in list(sorted(phones, key=lambda x: x.price, reverse=True)):
            phone.append(v)
    else:
        phone = phones

    context = {
        'phones': phone
    }
    return render(request, template, context)


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    template = 'product.html'
    context = {
        'phone': phone,
    }
    return render(request, template, context)
