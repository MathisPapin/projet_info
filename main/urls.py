from django.urls import path
from .views import check_age, home, not_allowed, graphique  

urlpatterns = [
    path('home/', home, name='home'),
    path('', check_age, name='check_age'),
    path('not_allowed/', not_allowed, name='not_allowed'),
    path('graphique/', graphique, name='graphique'),  
]
