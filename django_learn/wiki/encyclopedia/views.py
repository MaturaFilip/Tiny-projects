from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from . import util
from django.shortcuts import redirect
from markdown2 import Markdown


# redirect root / to /wiki/
def index(request):
    return redirect('main_page')


# render main page
def main_page(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# validate entries
def page(request, valid_entry):
    """
    Check if the entry exist and render md to html entry.html
    """
    entry_name = valid_entry
    markdowner = Markdown()
    if util.get_entry(valid_entry) != None:
        return render(request, "encyclopedia/entry.html", {
            "entry": markdowner.convert(util.get_entry(valid_entry)),
            "entry_name": entry_name
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "entry_name": entry_name
        })