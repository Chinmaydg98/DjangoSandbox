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
