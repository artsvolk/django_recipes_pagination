# Обработка запросов к рецептам
from django.http import HttpResponse
from django.shortcuts import render

# Словарь с рецептами
DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

# Отображение главной страницы
def index_view(request):
    return HttpResponse(
        "Рецепты:\n"
        "- /omlet/\n"
        "- /pasta/\n"
        "- /buter/\n\n"
        "Пример: /omlet/?servings=4"
    )

def recipe_view(request, dish):
    # Получение количества порций из параметров запроса
    servings = request.GET.get('servings')
    if servings and servings.isdigit():
        servings = int(servings)
    else:
        servings = 1

    # Получение рецепта по названию блюда
    recipe = DATA.get(dish)

    if recipe:
        # Умножение ингредиентов на количество порций
        scaled_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}
        context = {'recipe': scaled_recipe}
    else:
        context = {'recipe': None}

    return render(request, 'calculator/index.html', context)