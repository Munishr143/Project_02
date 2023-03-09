from Kaithi.views import *
from django.urls import path

app_name='something'


urlpatterns=[
    path('Hero/', Hero, name='Hero'),
    path('Villain', Villain, name='Villain'),
    path('Heroine/', Heroine, name='Heroine'),
]