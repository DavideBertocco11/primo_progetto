from django.urls import path
from prova_pratica_0.views import index3, somma, media
app_name="prova_pratica_0"
urlpatterns=[ 
    path('', index3, name='index3'),
    path('somma', somma, name='somma'),
    path('media', media, name='media'),
]