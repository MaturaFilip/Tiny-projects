# URLS in students app
from django.urls import path
from . import views

urlpatterns = [
    path("<studentsname>", views.allstudentsinfo),

]
