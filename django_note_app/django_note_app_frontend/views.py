from django.shortcuts import render
from django.http import HttpResponse
from django_note_app_frontend.models import Field
from django_note_app_frontend.forms import NoteForm


def home(request):
    template_name = "home.html"
    context = {
        "Fields": Field.objects.all(),
        "NoteForm": NoteForm(),
    }
    return render(request, "home.html", context)
