from django.http import HttpResponse


def index(request):
    """Homepage"""
    return HttpResponse('Hello this is index.')
