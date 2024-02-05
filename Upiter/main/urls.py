from django.urls import path
from . import views

urlpatterns = [
    path('', views.slider, name = "slider"),
    path("autoriz/", views.autoriz, name = "autoriz"),
    path('upiter/', views.upiter , name ="upiter"),
    path('exit/', views.exit, name = "exit" ),
    path('loadImage/', views.loadImage, name = "loadImage" ),
    path('setpage/<str:name>/', views.setpage, name = "setpage"),
    path('history/', views.history, name ="history"),
    path('transfer/', views.transfer, name = "transfer"),
    path("messenger/", views.messenger, name="messenger"),
    path('selectTransfer/', views.selectTransfer, name ="selectTransfer"),
    path("Transaction/", views.transaction,  name ="transaction"),
    path('transactionPage/', views.pageTransaction, name = "PTransac"),
    path('SetUsers/', views.SetUsers, name = 'SetUsers'),
    path('addMessage/', views.addMessage, name = 'addMessage'),
]