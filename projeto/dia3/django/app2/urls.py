from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home2'),
    path('app/',views.renderizar_home2, name='app')
]