from django.shortcuts import render
from django.http import HttpResponse

def calculate(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                return HttpResponse("Cannot divide by zero")
        else:
            return HttpResponse("Invalid operation")

        return render(request, 'result.html', {'result': result})

    return render(request, 'index.html')
