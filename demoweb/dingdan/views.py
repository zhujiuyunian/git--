from django.shortcuts import render
from .models import Dingdan
from useraccount.models import Useraccount

def show(request):
    buy = Dingdan.objects.filter(buyer=request.session.get('username'))
    appname1 =Useraccount.objects.filter(username=request.session.get('username')).first()
    if appname1 and appname1.appname :
        seller = appname1.appname
        sell = Dingdan.objects.filter(seller=seller)
    else:
        sell = None
    return render(request,'dingdanshow.html',{'buy':buy,'sell':sell})

