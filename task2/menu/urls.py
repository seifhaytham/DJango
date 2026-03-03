from django.urls import path
from . import views

app_name = "menu"

urlpatterns = [
    path("", views.meal_list, name="home"),          
    path("meals/", views.meal_list, name="meal_list"),
]