from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')


def ping(request):
    return render(request, 'ping.html')


def pong(request):
    # print(request)
    # print(dir(request))
    # print(request.get_full_path)
    # ball = request.GET.get('ball')
    # context = {
    #     'name' = ball,
    # }

    return render(request, 'pong.html', {'name' : request.GET.get('ball')})


def odd_even(request, _number):
    context = {
        "number": _number,
        "odd_even": "짝수" if _number % 2 == 0 else "홀수",
    }
    return render(request, "is_odd_even.html", context)


def calculate(request, _number1, _number2):
    context = {
        "number1": _number1,
        "number2": _number2,
    }
    return render(request, "calculate.html", context)


def randomlife(request):
    text = request.GET.get("_text")

    context = {
        "template_text": text,
    }
    return render(request, "randomlife.html", context)


def randomresult(request):
    name = request.GET.get("randomlife")
    lives = ["말", "고양이", "강아지", "사자", "돼지", "닭", "개구리"]

    life = random.choice(lives)
    context = {
        "randomresult": life,
        "name": name,
    }
    return render(request, "randomresult.html", context)