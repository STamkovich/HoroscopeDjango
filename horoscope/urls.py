from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FloatConverter, 'float')
urlpatterns = [
    path('', views.index),
    path('type', views.disaster_choice),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<float:sign_zodiac>/', views.get_mu_float_converters),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope_name'),  # name - это регистрация url
]
