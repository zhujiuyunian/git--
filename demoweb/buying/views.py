from django.shortcuts import render,redirect,HttpResponse
from .models import Products
from useraccount.models import Useraccount
from selling.models import Sellproduct
from dingdan.models import Dingdan
from datetime import datetime

# Create your views here.

def show(request):
    products=Products.objects.all()
    return render(request,'show.html',{"products":products})

def lis1(request):
    name1 = request.POST.get('name')
    buyname = request.POST.get('buyname')
    products = Products.objects.filter(name=name1,buyname=buyname)
    return render(request, 'buy.html', {'products': products})  # 渲染lis1.html模板,并传递商品数据

def lis2(request):
    num = float(request.POST.get('购买数量'))
    product_name = request.POST.get('name')
    id = request.POST.get('id')
    buy_name = request.POST.get('buyname')
    price = request.POST.get('price')
    product = Products.objects.filter(name=product_name,buyname=buy_name).first()
    try:
        if request.session['username'] :
            user = Useraccount.objects.filter(username=request.session['username']).first()
            user1 = Useraccount.objects.filter(appname=buy_name).first()
            productnumber = Products.objects.get(name=product_name).number
            if product :
                if product.price :
                    if productnumber:
                        if productnumber >= num:
                            if user:
                                if num * product.price < user.money:
                                    if product.number == None or product.number =='':
                                        product.number = 0.0
                                    if num == None or num =='' :
                                        num = 0.0
                                    product.number = product.number - num
                                    if product.number == 0.0:
                                        product.delete()
                                    else:
                                        product.save()
                                    user.money = user.money - num * product.price
                                    user.save()
                                    if user1:
                                        user1.money = user1.money + num * product.price
                                        user1.save()
                                    sellproduct =  Sellproduct.objects.filter(name=product_name,appname=buy_name).first()
                                    if sellproduct:
                                        sellproduct.number = sellproduct.number - num
                                        if sellproduct.number <= 0:
                                            sellproduct.delete()
                                        else:
                                            sellproduct.save()
                                    paytime = datetime.now()
                                    paytime = str(paytime.strftime('%Y-%m-%d %H:%M:%S'))
                                    dingdan = Dingdan(buyer=request.session['username'],productname=product_name,productnumber=num,productprice=price,seller=buy_name,paymoney=float(price)*float(  num),paytime=paytime)
                                    dingdan.save()
                                    return redirect('/buying/buy/buyresult/result/')
                                else:
                                    # 购买金额不够
                                    return HttpResponse('余额不足，购买失败')
                            else:
                                return HttpResponse('出现错误，请稍后重试')
                        else:
                            return HttpResponse('货品数量不够，请等待补货')
                    else:
                        return HttpResponse('出现错误，请重试')
                else:
                    return HttpResponse('购买失败，请稍后重试')
            else:
                return HttpResponse('出现错误，请重试')
        else:
            return redirect('/useraccount/')
    except KeyError as key:
        return redirect('/useraccount/')

def search(request):
    name=request.POST.get('search')
    products=Products.objects.filter(name=name)
    return render(request,'searchresult.html',{'products':products})

def buyresult(request):
    return render(request,'buyresult.html')