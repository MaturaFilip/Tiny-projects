from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


# request = žádost; když se zažádá, co se má vrátit?
def allstudentsinfo(request, studentsname):
    try:

        return HttpResponse(f"Info o {studentsname}")
    except:
        return HttpResponseNotFound("Zadáno špatné mono")






