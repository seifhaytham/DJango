from django.shortcuts import render

# in-memory list of meals
MEALS = [
    {"name": "Pizza", "price": 12.5, "available": True, "category": "Italian"},
    {"name": "Burger", "price": 8.0, "available": True, "category": "American"},
    {"name": "Sushi", "price": 15.0, "available": False, "category": "Japanese"},
    {"name": "Tacos", "price": 7.5, "available": True, "category": "Mexican"},
    {"name": "Pasta", "price": 11.0, "available": True, "category": "Italian"},
]


def meal_list(request):
    """Render a list of meals optionally filtered by name and/or category."""
    qs = MEALS
    name_query = request.GET.get("name", "").strip().lower()
    category_query = request.GET.get("category", "").strip().lower()

    if name_query:
        qs = [m for m in qs if name_query in m["name"].lower()]
    if category_query:
        qs = [m for m in qs if category_query in m["category"].lower()]

    all_categories = sorted({m["category"] for m in MEALS})
    context = {
        "meals": qs,
        "name_query": request.GET.get("name", ""),
        "category_query": request.GET.get("category", ""),
        "categories": all_categories,
    }
    return render(request, "menu/meal_list.html", context)
