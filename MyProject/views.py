from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    """Homepage"""
    return render(request, 'index.html')


@login_required
def calculate(request):
    """Calculation"""
    expression = request.POST.get('inExpression', '')
    print(expression)
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
