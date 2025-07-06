from django.urls import path
from . import views

urlpatterns=[
    path('',views.login),
    path('login/',views.loginjudge),
    path('register/',views.register),
    path('userinformation/',views.userinf),
    path('userinformation/reset/',views.resetandquit), # type: ignore
]