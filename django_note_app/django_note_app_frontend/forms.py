from django import forms
from django_note_app_frontend.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['field', 'text']
        