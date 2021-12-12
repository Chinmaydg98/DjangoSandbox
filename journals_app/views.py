from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def JournalsPage(request):
    """
    List all Journals
    """
    journals = Journal.objects.order_by('date_added')
    context = {'journals': journals}
    return render(request, 'journals_app/journals.html', context)


def newJournal(request):
    """
    Creation of new journals is done here.
    Uses a ModelForm (JournalForm)
    """
    if request.method != 'POST':
        # Means no form data received, hence create new form
        form = JournalForm()
    else:
        # Form data received, hence validate, save form and redirect
        form = JournalForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('journals')

    context = {'form': form}
    return render(request, 'journals_app/newJournal.html', context)


def journal(request, journal_id):
    """
    Drilldown for each journal, shows list of entries
    """
    journalItem = Journal.objects.get(id=journal_id)
    entries = journalItem.entry_set.order_by('-date_added')
    context = {'journal': journalItem.title, 'entries': entries}
    return render(request, 'journals_app/journal.html', context)
