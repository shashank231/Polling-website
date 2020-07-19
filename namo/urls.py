from django.urls import path
from .import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('create', views.create, name='create'),
    path('vote/<str:pk>/', views.vote, name='vote'),
    path('result/<str:pk>/', views.result, name='result'),
    path('viewresult/<str:pk>/', views.viewresult, name='viewresult'),
    path('deletepoll/<str:pk>/', views.delete, name='delete'),
    path('', views.intro, name='intro'),
]