from django import forms
from django_note_app_frontend.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["field", "text"]


class DeleteCheck(forms.Form):
    checkbox = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), label=False)