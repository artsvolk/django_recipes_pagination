# Маршрутизация запросов к рецептам
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),       # ← корень
    path('<dish>/', views.recipe_view, name='recipe'),
]