from django.urls import path
from . import views as views_fake


urlpatterns = [
    path('actor', views_fake.get_info_actor),
    path('gwr', views_fake.get_guinness_world_records),
]