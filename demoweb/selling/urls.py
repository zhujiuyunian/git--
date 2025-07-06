from django.urls import path
from . import views

urlpatterns=[
    path('',views.sellshow),
    path('up/',views.up),
    path('down/',views.down),
    path('up/result/',views.upresult),
    path('down/result/',views.downresult),
    path('up/result/upresult/',views.uppage),
    path('down/result/downresult/',views.downpage),
]