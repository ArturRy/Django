from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import  csv

def index(request):
    return redirect(reverse('bus_stations'))










with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    CONTENT = [(row['Name'], row['Street'], row['District']) for row in reader]



def bus_stations(request):

    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(str(CONTENT), 10)
    page = paginator.get_page(page_number)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
