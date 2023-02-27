from django.shortcuts import render
from django.http import HttpResponseRedirect
from django_note_app_frontend.models import Field, Note
from django_note_app_frontend.forms import NoteForm
from django.views.decorators.http import require_GET, require_POST
from django.urls import reverse


@require_GET
def home(request):
    template_name = "home.html"
    context = {
        "Fields": Field.objects.all(),
        "Notes": Note.objects.order_by("-created_at"),
        "NoteForm": NoteForm(),
    }
    return render(request, "home.html", context)


@require_POST
def new_note(request):
    form = NoteForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        n = Note(field=data["field"], text=data["text"])
        n.save()
    return HttpResponseRedirect(reverse("note:home"))
