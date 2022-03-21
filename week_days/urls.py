from django.urls import path
from . import views as week_days

urlpatterns = [
    path('', week_days.plans_week),
    path('<int:day_weeks>', week_days.get_index_week),
    path('<day_weeks>', week_days.get_plans_week, name='weeks_day'),

]
