from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.go_new, name='go_new'),
    path('write/', views.write, name='write'),
]