from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('simulador/<int:pk>/', views.simulador, name='simulador'),
    path('busca_pagina/<int:pk>/<slug:choice>/', views.busca_pagina, name='busca_pagina'),
]

