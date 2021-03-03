from django.contrib import admin
from django.urls import path

from .views import *
urlpatterns = [
    path("",home_view),
    path("api",apiview,name="api"),
    path('task-details/<int:pk>/',taskDetails,name='task-details'),
    path('update_task/<int:pk>/',show, name='update_task'),
    path('delete/<str:pk>/',deleteTask, name='delete'),
    path("",index),
    path("signup",signup,name="signup"),
    path("login",login,name="login"),
    path("cartvalue",cartvalue,name="cartvalue"),
    path("logout",logout,name="logout"),
    path("cart",cart,name="cart"),
    path("checkout",checkout,name="checkout"),

]
