from django.shortcuts import render


def get_info_actor(request):
    data = {
        "year_born": '1964',
        "city_born": ' Бейрут',
        "movie_name": '«Матрица»',
    }
    return render(request, 'fake/popular_actor.html', context=data)


def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'fake/guinnessworldrecords.html', context=context)
