from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('',login, name="login"),
    path('logout/',logout, name="logout"),
    path('home/',home, name="home"),
    path('routinelist/',routinelist,name="routinelist"),
    path('createroutine/',createroutine,name="createroutine"),
    path('deleteroutine/<int:routineid>/',deleteroutine,name="deleteroutine"),
]
