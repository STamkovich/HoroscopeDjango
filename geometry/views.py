from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import math
from django.urls import reverse


def get_rectangle_area(request):
    return render(request, 'geometry/rectangle.html')


def get_square_area(request):
    return render(request, 'geometry/square.html')


def get_circle_area(request):
    return render(request, 'geometry/circle.html')


def rectangle(request, width, height):
    response = width * height
    return HttpResponse(f'Площадь прямоугольника размером {width}х{width} равна {response}')


def square(request, width):
    response = width * width
    return HttpResponse(f'Площадь квадрата размером {width}х{width} равна {response}')


def circle(request, radius):
    response = math.pi * (radius ** 2)
    return HttpResponse(f'Площадь круга c радиусом {radius} ровна {int(response)}')
