from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
list_of_days = {
    "monday": "Jít nakoupit",
    "tuesday": "učit se python",
    "wednesday": "vynést koš",
    "thursday": "dojít nakoupit",
    "friday": "naprogramovat hru",
    "saturday": "sedět",
    "sunday": "cvičit"
}

def index(request):
    days = list(list_of_days.keys())

    content = "<ul>"
    for day in days:
        url = reverse("days_tasks", args=[day])
        content += f"<li><a href='{url}'>{day.capitalize()}</a></li>"
    content += "</ul>"

    return HttpResponse(content)

def daynumber(request, dayinweek_number):
    days_names = list(list_of_days.keys())

    if dayinweek_number > len(days_names):
        return HttpResponseNotFound("špatné číslo dne")
    redirect_day = days_names[dayinweek_number - 1]
    # tvorba url
    redirect_path = reverse("days_tasks", args=[redirect_day])
    return HttpResponseRedirect(redirect_path)


def daytext(resuest, dayinweek_string):
    try:
        task = list_of_days[dayinweek_string]
        formated_task = f"<h1>{task}</h1>"
        return HttpResponse(formated_task)
    except:
        return HttpResponseNotFound("Špatně zadaný údaj")


