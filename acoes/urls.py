from django.urls import path

from . import views

urlpatterns = [
    path('<str:codigo>/', views.AcoesView.as_view(), name='grafico-acoes'),
    path('', views.IndexView.as_view(), name='index-acoes')
]