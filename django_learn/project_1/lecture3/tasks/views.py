from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

#tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    #message = forms.CharField(widget=forms.Textarea, label="Message")
    #priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

# Create your views here.

def index(request):
    # is there already a list of task in that session
    # if not, create empty list of tasks
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        # form -> contain all data user submit
        form = NewTaskForm(request.POST)
        # is data valid -> True, not valid ->  False
        if form.is_valid():
            # dictionary where keys are the form filed names and values
            # are validated
            # zde si value z "task"
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            # redirect user to "tasks:index"
            return HttpResponseRedirect(reverse("tasks:index",  kwargs={"valid_entry": search}))
        else:
            return render(request, "task/add.html", {
                # return form he submitted (they can see error)
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })