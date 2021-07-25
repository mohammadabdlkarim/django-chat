from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('<str:room>/', room, name="room"),
    path('checkview', checkview, name="check"),
    path('send', send, name="send"),
    path('getMessages/<str:room>/', get_messages, name="get_messages"),

]
