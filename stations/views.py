# Чтение данных из CSV и реализация пагинации
import csv
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render

def bus_stations(request):
    bus_stations_list = []
    with open(settings.BUS_STATION_CSV, encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bus_stations_list.append(row)

    page_number = request.GET.get('page', 1)
    paginator = Paginator(bus_stations_list, 10)
    page_obj = paginator.get_page(page_number)

    context = {
        'bus_stations': page_obj,
    }
    return render(request, 'stations/index.html', context)