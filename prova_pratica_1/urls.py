from django.urls import path
from prova_pratica_1.views import view_a, view_b 
app_name="prova_pratica_1"
urlpatterns=[ 
    path('materie', view_a, name='materie'),
    path('voti', view_b, name='voti'),
]