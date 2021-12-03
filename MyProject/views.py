from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Homepage"""
    return render(request, 'index.html')


def calculate(request):
    """Calculation"""
    expression = request.GET.get('inExpression', '')

    if expression == '':
        return render(request, 'calculator.html')
    if expression != '':
        try:
            result = eval(expression)
        except SyntaxError:
            return HttpResponse("Syntax Error. Please input a valid expression")
        except ZeroDivisionError:
            return HttpResponse("Division by zero")
        except NameError:
            return HttpResponse("Syntax Error. Please input a valid expression")
        else:
            return HttpResponse(result)
