from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('newUser/',views.newAppUser, name='newUser'),
    path('newUser/welcome/', views.saveNewUser, name='welcome')

    ]
