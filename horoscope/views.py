from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

disaster_zodiac_dict = {'fire': ['aries', 'leo', 'sagittarius'],
                        'earth': ['taurus', 'virgo', 'capricorn'],
                        'air': ['gemini', 'libra', 'aquarius'],
                        'water': ['cancer', 'scorpio', 'pisces']

                        }


def get_mu_float_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали вещественное число - {sign_zodiac}')


def index(request):
    zodiacs = list(zodiac_dict)
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse("horoscope_name", args=[sign])
        li_elements += f"<li> <a href='{redirect_path}'>{sign.title()}</a> </li>"
    response = f'''
    <ul>
    {li_elements}
    </ul>
    '''
    return HttpResponse(response)


def disaster_choice(request):
    disasters = list(disaster_zodiac_dict)
    li_disaster = ''
    for dis in disasters:
        redirect_path = reverse('desic_name', args=[dis])
        li_disaster += f"<li> <a href='{redirect_path}'>{dis.title()}</a> </li>"
    response1 = f'''
        <ul>
        {li_disaster}
        </ul>
        '''
    return HttpResponse(response1)


def type_description(request, type_des):
    choice_type_des = disaster_zodiac_dict.get(type_des)
    if choice_type_des:
        zodiac_list = ''
        for el in disaster_zodiac_dict[type_des]:
            redirect_path = reverse("horoscope_name", args=[el])
            zodiac_list += f"<li> <a href='{redirect_path}'>{el.title()}</a> </li>"
        response2 = f'''
            <ul>
            {zodiac_list}
            </ul>
            '''
        return HttpResponse(response2)


def get_info_about_sign_zodiac(request, sign_zodiac):
    # конвертация в словарь
    description = zodiac_dict.get(sign_zodiac, None)
    response = render_to_string('horoscope/info_zodiac.html')
    return HttpResponse(response)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Передан неправильный порядковый номер знака зодиака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse("horoscope_name", args=(name_zodiac,))  # функция реверс
    # Class Redirect - перенаправление адреса
    return HttpResponseRedirect(redirect_url)
