"""Metodos URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from M import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.test, name="test"),
    path('gtest/', views.gtest, name="gtest"),
    path('welcome/', views.welcome, name="welcome"),
    path('metodos/', views.metodos, name="metodos"),
    path('graficador/', views.graficador, name="graficador"),
    path('ayuda/', views.ayuda, name="ayuda"),
    path('BI/', views.BI, name="BI"),
    path('B/', views.B, name="B"),
    path('PF/', views.PF, name="PF"),
    path('PFi/', views.PFi, name="PFi"),
    path('NR/', views.NR, name="NR"),
    path('SEC/', views.SEC, name="SEC"),
    path('RM/', views.RM, name="RM"),
    path('EG1/', views.EG1, name="EG1"),
    path('EG2/', views.EG2, name="EG2"),
    path('EG3/', views.EG3, name="EG3"),
    path('LUS/', views.LUS, name="LUS"),
    path('LUP/', views.LUP, name="LUP"),
    path('Cr/', views.Cr, name="Cr"),
    path('DO/', views.DO, name="DO"),
    path('CH/', views.CH, name="CH"),
    path('IT/', views.IT, name="IT"),
    path('Va/', views.Va, name="Va"),
    path('NDD/', views.NDD, name="NDD"),
    path('LA/', views.LA, name="LA"),
    path('SP/', views.SP, name="SP"),
]
