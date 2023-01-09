from django.urls import path
from prova_pratica_2.views import auto, noleggi
app_name="prova_pratica_2"
urlpatterns=[
    path('', auto, name="auto"),
    path('noleggi', noleggi, name="noleggi"),
]