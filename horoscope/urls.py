from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('type', views.disaster_choice),
    path('type/<type_des>', views.type_description, name='desic_name'),
    path('<int:month>/<day>', views.get_info_by_data),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope_name'),  # name - это регистрация url
]
