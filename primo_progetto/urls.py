"""primo_progetto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import index_generale

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prima_app/',include('prima_app.urls',namespace="prima_app")),
    path('seconda_app/',include('seconda_app.urls',namespace="seconda_app")),
    path('',index_generale, name="index_generale"),
    path('prova_pratica_0/', include('prova_pratica_0.urls', namespace="prova_pratica_0"))
]
