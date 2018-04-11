from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('nuevo/', views.new_todo),
    path('change-status/', views.change_status),
]
