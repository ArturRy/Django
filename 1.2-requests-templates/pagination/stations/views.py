from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def cont_reader():
    result = []
    with open('data-398-2018-08-30.csv', newline='', encoding='UTF-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            result.append(line)
    return result


CONTENT = cont_reader()


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
