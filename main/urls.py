from django.urls import path
from .views import check_age, home

urlpatterns = [
    path('home/', home, name='home'),
    path('', check_age, name='check_age')
]
