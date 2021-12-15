from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
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
    context = {'journal': journalItem.title, 'entries': entries, 'journal_id': journal_id}
    return render(request, 'journals_app/journal.html', context)


def newEntry(request):
    """
    Creation of new Entries done here.
    Uses ModelForm (EntryForm)
    """
    journal_id = request.GET.get('journal_id')
    print(journal_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/journal/'+journal_id+'/')

    context = {'form': form, 'journal_id': journal_id}
    return render(request, 'journals_app/newEntry.html', context)
