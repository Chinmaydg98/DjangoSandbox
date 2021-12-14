from django import forms

from .models import *


class JournalForm(forms.ModelForm):
    """
    Model form for Journals
    TD: Style all fields
    """

    class Meta:
        model = Journal
        fields = ['title']
        labels = {'title': 'Journal Title'}


class EntryForm(forms.ModelForm):
    """
    Model form for Entries
    TD: Style all fields
    """
    class Meta:
        model = Entry
        fields = ['journal', 'text']
        labels = {'journal': 'Journal', 'text': ''}
