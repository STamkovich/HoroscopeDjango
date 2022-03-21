from django.urls import path
from . import views as views_geometry

urlpatterns = [
    path('get_rectangle_area', views_geometry.get_rectangle_area),
    path('get_square_area/<int:width>', views_geometry.get_square_area),
    path('get_circle_area/<int:radius>', views_geometry.get_circle_area),
    path('rectangle/<int:width>/<int:height>', views_geometry.rectangle, name='rectangle'),
    path('square/<int:width>', views_geometry.square, name='square'),
    path('circle/<int:radius>', views_geometry.circle, name='circle'),
]
