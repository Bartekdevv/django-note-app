from django.shortcuts import render
from django.http import HttpResponseRedirect
from django_note_app_frontend.models import Field, Note
from django_note_app_frontend.forms import NoteForm
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import logout

@login_required
@require_GET
def home(request):
    template_name = "home.html"
    context = {
        "Fields": Field.objects.all(),
        "Notes": Note.objects.order_by("-created_at"),
        "NoteForm": NoteForm(),
    }
    return render(request, "home.html", context)

@login_required
@require_POST
def new_note(request):
    form = NoteForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        n = Note(field=data["field"], text=data["text"])
        n.save()
    return HttpResponseRedirect(reverse("note:home"))

def redirect(request):
    return HttpResponseRedirect("/home")

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/home")