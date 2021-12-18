from django.shortcuts import render, redirect
from .models import Journal, Entry
from .forms import JournalForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.

@login_required
def JournalsPage(request):
    """
    List all Journals
    """
    journals = Journal.objects.filter(owner=request.user).order_by('date_added')
    context = {'journals': journals}
    return render(request, 'journals_app/journals.html', context)


@login_required
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
            JournalFormData = form.save(commit=False)
            JournalFormData.owner = request.user
            JournalFormData.save()
            return redirect('journals')

    context = {'form': form}
    return render(request, 'journals_app/newJournal.html', context)


@login_required
def journal(request, journal_id):
    """
    Drilldown for each journal, shows list of entries
    """
    journalItem = Journal.objects.get(id=journal_id)

    # Check if Journal belongs to user
    if journalItem.owner != request.user:
        raise Http404

    entries = journalItem.entry_set.order_by('-date_added')
    context = {'journal': journalItem.title, 'entries': entries, 'journal_id': journal_id}
    return render(request, 'journals_app/journal.html', context)


@login_required
def newEntry(request):
    """
    Creation of new Entries done here.
    Uses ModelForm (EntryForm)
    """
    journal_id = request.GET.get('journal_id')

    # Check owner
    journalItem = Journal.objects.get(id=journal_id)
    if journalItem.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            EntryFormData = form.save(commit=False)
            EntryFormData.journal = journalItem
            EntryFormData.save()
            return redirect('/journal/'+journal_id+'/')

    context = {'form': form, 'journal_id': journal_id}
    return render(request, 'journals_app/newEntry.html', context)
