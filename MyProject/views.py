from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Homepage"""
    return render(request, 'index.html')


def calculate(request):
    """Calculation"""
    expression = request.GET.get('inExpression', '')

    try:
        result = eval(expression)
    except SyntaxError:
        return HttpResponse("Syntax Error. Please input a valid expression")
    except ZeroDivisionError:
        return HttpResponse("Division by zero")
    else:
        return HttpResponse(result)
