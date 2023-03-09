from Vikram.views import *
from django.urls import path

app_name='nothing'

urlpatterns=[
    path('Hero/', Hero, name='Hero'),
    path('Villain/', Villain, name='Villain'),
    path('Heroine/', Heroine, name='Heroine')
]