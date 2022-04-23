from django.urls import path
from .views import *

urlpatterns=[
    path('home',home,name="home"),
    path('',sign,name="login"),
    path('register',register,name="register"),
    path('logout',logout_view,name="logout")
]