from django.urls import path
from . import views

urlpatterns = [
    path('', views.slider, name = "slider"),
    path("autoriz/", views.autoriz, name = "autoriz"),
    path('upiter/', views.upiter , name ="upiter"),
    path('exit/', views.exit, name = "exit" ),
    path('loadImage/', views.loadImage, name = "loadImage" ),
    path('setpage/<str:name>/', views.setpage, name = "setpage"),
]