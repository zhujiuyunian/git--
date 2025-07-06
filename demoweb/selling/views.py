from django.shortcuts import render,redirect,HttpResponse
from .models import Sellproduct
from buying.models import Products
from useraccount.models import Useraccount

# Create your views here.
def sellshow(request):
    if request.session.get('username') != None:
        return render(request,'start1.html')
    else:
        return redirect('/useraccount/')


def up(request):    
    return render(request,'huowuup.html')
def down(request):
    products = Sellproduct.objects.filter(username=request.session['username'])
    return render(request,'huowudown.html', {'products':products})

def upresult(request):
    name1 = request.POST.get('productname')
    price = request.POST.get('productprice')
    number = request.POST.get('productnumber')
    img_url = request.POST.get('url')
    description = request.POST.get('description')
    account = Useraccount.objects.filter(username=request.session['username']).first()
    if not account:
        buyname = '匿名'
    else:
        buyname = account.appname
    if name1 :
        if not Sellproduct.objects.filter(name=name1,appname=buyname):
            if number:
                if price:
                    if not number:
                        number = 0.0
                    if not price:
                        price = 0.0
                    products=Products(name=name1,price=float(price),number=float(number),img_url=img_url,description=description,buyname=buyname)
                    sellproduct=Sellproduct(name=name1,price=float(price),number=float(number),img_url=img_url,description=description,appname=buyname,username=request.session['username'])
                    products.save()
                    sellproduct.save()
                    return redirect('/selling/up/result/upresult/')
                return HttpResponse('请补全商品价格')
            return HttpResponse('请补全商品上架数量')          
        else:
            products=Products.objects.filter(name=name1).first()
            sellproduct=Sellproduct.objects.filter(name=name1).first()
            if not number:
                number = 0.0
            if not price:
                 if sellproduct:
                     if sellproduct.price:
                         price = float(sellproduct.price)
            if not description:
                if sellproduct:
                    if sellproduct.description:
                         description = sellproduct.description
            if not img_url:
                if sellproduct:
                    if sellproduct.img_url:
                         img_url = sellproduct.img_url
            if products:
                if products.number:
                    products.number = products.number + float(number)
                    products.price = price
                    products.description = description
                    products.img_url = img_url
                    products.save()
            if sellproduct:
                if sellproduct.number:
                    sellproduct.number = sellproduct.number + float(number)
                    sellproduct.price = price 
                    sellproduct.description = description
                    sellproduct.img_url = img_url
                    sellproduct.save()
            return redirect('/selling/up/result/upresult/')  
    else:
        return HttpResponse('请补全商品名称')


def downresult(request):
    product_name = request.POST.get('chaxun')
    username = request.session['username']
    chaxunname = Useraccount.objects.filter(username=username).first()
    number = request.POST.get('number')
    print(number)
    if number:
        if chaxunname and chaxunname.appname :
            buyname=chaxunname.appname
            product = Products.objects.filter(name=product_name,buyname=buyname).first()
            sellproduct = Sellproduct.objects.filter(name=product_name,appname=buyname).first()
            if product and sellproduct:
                if product.number and sellproduct.number:
                    if float(number) < sellproduct.number:
                        sellproduct.number = sellproduct.number - float(number)
                        product.number = product.number - float(number)
                        sellproduct.save()
                        product.save()
                    else:
                        sellproduct.delete()
                        product.delete()
        return redirect('/selling/down/result/downresult/')
    else:
        return HttpResponse('请填写下架数量')

def uppage(request):
    return HttpResponse('上架成功')

def downpage(request):
    return HttpResponse('下架成功')