from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

teachers_info = {
    "snape": "Teacher Snape",
    "brumbal": "Teacher Brumby",
}


def allteachersinfo(request, teachername):
    try:
        info = teachers_info[teachername]
        return HttpResponse(info)
    except:
        return HttpResponseNotFound("Not found")