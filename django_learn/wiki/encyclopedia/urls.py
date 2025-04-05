from django.urls import path

from . import views

urlpatterns = [
    # "" routnout na /wiki
    path("", views.index, name="index"),
    # "/wiki" main page
    path("wiki/", views.main_page, name="main_page"),
    path("wiki/<str:valid_entry>", views.page, name="page")
]
