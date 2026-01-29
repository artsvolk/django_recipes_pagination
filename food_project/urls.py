# Основная маршрутизация проекта
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bus_stations/', include('stations.urls')),  # ← СНАЧАЛА конкретные маршруты
    path('', include('recipes.urls')),                # ← ПОТОМ общий маршрут <dish>/
]