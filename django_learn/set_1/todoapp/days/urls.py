from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:dayinweek_number>", views.daynumber),
    # z urls.py days/ to days_tasks
    path("<str:dayinweek_string>", views.daytext, name="days_tasks"),
]
