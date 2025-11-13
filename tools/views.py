from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import math

@require_http_methods(["GET", "POST"])
def home(request):
    return render(request, 'home.html')

@require_http_methods(["GET", "POST"])
def calculator(request):
    result = None
    if request.method == 'POST':
        try:
            n1 = float(request.POST['num1'])
            n2 = float(request.POST['num2'])
            op = request.POST['operation']

            if op == '+':
                result = n1 + n2
            elif op == '-':
                result = n1 - n2
            elif op == '*':
                result = n1 * n2
            elif op == '/':
                result = n1 / n2 if n2 != 0 else 'Error: ÷0'
        except Exception:
            result = 'Invalid input'

    return render(request, 'calculator.html', {'result': result})

@require_http_methods(["GET", "POST"])
def even_odd(request):
    result = None
    if request.method == 'POST':
        try:
            num = int(request.POST['number'])
            result = f"{num} is {'Even' if num % 2 == 0 else 'Odd'}"
        except ValueError:
            result = 'Please enter an integer'

    return render(request, 'evenodd.html', {'result': result})

@require_http_methods(["GET", "POST"])
def factorial(request):
    result = None
    if request.method == 'POST':
        try:
            n = int(request.POST.get('number', 0))
            if n < 0:
                result = 'Factorial not defined for negative numbers'
            else:
                result = math.factorial(n)
        except ValueError:
            result = 'Enter a valid integer'

    return render(request, 'factorial.html', {'result': result})
def fibonacci(request):
    result = 0
    if request.method == 'POST':
        try:
            n = int(request.POST.get('number', 0))
            if n < 0:
                result = 'Fibonacci not defined for negative numbers'
            else:
                a, b = 0, 1
                for _ in range(n):
                    a, b = b, a + b
                result = a
        except ValueError:
            result = 'Enter a valid integer'
    return render(request, 'fibonacci.html', {'result': result})
def bmi(request):
    bmi_r=0
    category=""
    if request.method == 'POST':
        try:
            weight = float(request.POST['weight'])
            height_cm = float(request.POST['height'])
            if height_cm <= 0 or weight <= 0:
                raise ValueError
            height_m = height_cm / 100
            bmi_r = round(weight / (height_m ** 2), 2)
            if bmi_r < 18.5:
                category = 'Underweight'
            elif bmi_r < 25:
                category = 'Normal'
            elif bmi_r < 30:
                category = 'Overweight'
            else:
                category = 'Obese'
        except:
            bmi_r = 'Invalid input'
            category = 'Error'

    return render(request, 'bmi.html', {
        'bmi': bmi_r,
        'category': category
    })

import math

@require_http_methods(["GET", "POST"])
def prime_checker(request):
    result = 0
    is_prime = ""

    if request.method == 'POST':
        try:
            num = int(request.POST['number'])
            if num <= 1:
                result = f"{num} is NOT a prime number"
                is_prime = False
            elif num == 2:
                result = f"{num} is a prime number"
                is_prime = True
            elif num % 2 == 0:
                result = f"{num} is NOT a prime number (divisible by 2)"
                is_prime = False
            else:
                # Check odd divisors up to sqrt(n)
                is_prime = True
                for i in range(3, int(math.sqrt(num)) + 1, 2):
                    if num % i == 0:
                        result = f"{num} is NOT a prime number (divisible by {i})"
                        is_prime = False
                        break
                if is_prime:
                    result = f"{num} is a prime number"
        except ValueError:
            result = "Error: Please enter a valid integer"
            is_prime = False

    return render(request, 'prime.html', {
        'result': result,
        'is_prime': is_prime
    })


from datetime import datetime
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
@require_http_methods(["GET", "POST"])
def age_calculator(request):
    age = None
    birth_date = None

    if request.method == 'POST':
        try:
            birth_str = request.POST['birth_date']
            birth_date = datetime.strptime(birth_str, '%Y-%m-%d').date()
            today = datetime.today().date()

            if birth_date > today:
                age = "Error: Birth date cannot be in the future"
            else:
                years = today.year - birth_date.year
                months = today.month - birth_date.month
                days = today.day - birth_date.day

                if days < 0:
                    months -= 1
                    days += (today.replace(day=1) - today.replace(day=1, month=today.month-1 if today.month > 1 else 12, year=today.year-1 if today.month == 1 else today.year)).days
                if months < 0:
                    years -= 1
                    months += 12

                age = f"{years} years, {months} months, {days} days"
        except ValueError as e:
            age = "Error: Please enter a valid date"

    return render(request, 'age.html', {
        'age': age,
        'birth_date': request.POST.get('birth_date') if request.method == 'POST' else ''
    })

def simple_interest(request):
    result = None
    principal = rate = time = None

    if request.method == 'POST':
        try:
            principal = float(request.POST.get('principal', 0))
            rate = float(request.POST.get('rate', 0))
            time = float(request.POST.get('time', 0))

            if principal <= 0 or rate <= 0 or time <= 0:
                result = {"error": "All values must be greater than 0"}
            elif rate > 100:
                result = {"error": "Rate cannot exceed 100%"}
            else:
                si = (principal * rate * time) / 100
                total = principal + si
                result = {
                    "si": round(si, 2),
                    "total": round(total, 2),
                    "formula": f"(${principal} × {rate}% × {time}) / 100"
                }
        except ValueError:
            result = {"error": "Please enter valid numbers only"}

    return render(request, 'simple_interest.html', {
        'result': result,
        'principal': principal,
        'rate': rate,
        'time': time
    })
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def table_generator(request):
    table = None
    number = rows = None

    if request.method == 'POST':
        try:
            number = int(request.POST.get('number', 0))
            rows = int(request.POST.get('rows', 10))

            if number <= 0 or rows <= 0:
                table = {"error": "Both number and rows must be positive"}
            elif number > 1000 or rows > 100:
                table = {"error": "Number ≤ 1000, Rows ≤ 100 for performance"}
            else:
                # Generate multiplication table
                table = {
                    "number": number,
                    "rows": rows,
                    "data": [
                        {"multiplier": i, "result": number * i}
                        for i in range(1, rows + 1)
                    ]
                }
        except ValueError:
            table = {"error": "Please enter valid integers"}

    return render(request, 'table.html', {
        'table': table,
        'number': number,
        'rows': rows
    })

def cube_calculator(request):
    result = None
    number = None

    if request.method == 'POST':
        try:
            number = float(request.POST.get('number', 0))
            if number == 0:
                result = {"cube": 0, "formula": "0³ = 0"}
            else:
                cube = number ** 3
                result = {
                    "number": number,
                    "cube": round(cube, 6),
                    "formula": f"{number}³ = {round(cube, 6)}"
                }
        except ValueError:
            result = {"error": "Please enter a valid number"}

    return render(request, 'cube.html', {
        'result': result,
        'number': number
    })
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def square_calculator(request):
    result = None
    number = None

    if request.method == 'POST':
        try:
            number = float(request.POST.get('number', 0))
            square = number ** 2
            result = {
                "number": number,
                "square": round(square, 6),
                "formula": f"{number}² = {round(square, 6)}"
            }
        except ValueError:
            result = {"error": "Please enter a valid number"}

    return render(request, 'square.html', {
        'result': result,
        'number': number
    })



def about(request):
    return render(request, 'about.html')