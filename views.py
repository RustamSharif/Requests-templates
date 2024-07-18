
from django.http import JsonResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 100,
        'сыр, г': 50,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def recipe_detail(request, recipe):
    servings = int(request.GET.get('servings', 1))
    if recipe in DATA:
        ingredients = {item: amount * servings for item, amount in DATA[recipe].items()}
        context = {'recipe': ingredients}
        return JsonResponse(context)
    else:
        return JsonResponse({'error': 'Recipe not found'}, status=404)