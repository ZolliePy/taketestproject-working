from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="TakeTest-Home"),
    path('home/', views.home, name="TakeTest-Home"),
    path('about/', views.about, name="TakeTest-About"),
]
