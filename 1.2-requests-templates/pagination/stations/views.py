from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import  csv

def index(request):
    return redirect(reverse('bus_stations'))









with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    info = []
    for row in reader:
        info.append([row['Name'], row['Street'], row['District']])

CONTENT = [(i) for i in info]
def bus_stations(request):
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(1)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': paginator,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
