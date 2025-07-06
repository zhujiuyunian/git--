from django.urls import path
from . import views

urlpatterns=[
    path('',views.show),
    path('buy/',views.lis1),
    path('buy/buyresult/', views.lis2),
    path('buy/buyresult/result/',views.buyresult),
    path('search/',views.search),
]