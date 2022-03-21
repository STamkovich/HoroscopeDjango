from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

day_week_dict = {'monday': 'Учиться',
                 'tuesday': 'Опять учиться'}


def plans_week(request):
    return render(request, 'week_days/greeting.html')


def get_plans_week(request, day_weeks):
    return HttpResponse(day_week_dict[day_weeks])


def get_index_week(request, day_weeks):
    number = list(day_week_dict)
    if day_weeks > len(number):
        return HttpResponseNotFound(f"Неверный номер дня - {day_weeks}")
    number_day = number[day_weeks - 1]
    redirect_path = reverse('weeks_day', args=[number_day])
    return HttpResponseRedirect(redirect_path)
