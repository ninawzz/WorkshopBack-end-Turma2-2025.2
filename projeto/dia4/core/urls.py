from django.urls import path, include
from . import views

urlpatterns = [
    path('',  views.home, name='home'), 
    path('consulta_cep/', views.consulta_cep, name='consulta_cep'),
]