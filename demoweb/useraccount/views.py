from django.shortcuts import render,redirect
from .models import Useraccount
# Create your views here.

def login(request):
    if request.session.get('username') != None:
        return redirect('/useraccount/userinformation/')
    else:
        userinformation=Useraccount.objects.all()
        return render(request,'login.html',{'userinformation':userinformation})

def loginjudge(request):
    result1 = request.POST.get('action')
    username1 = request.POST.get('username')  # 注意这里是 username，不是 usename
    password1 = request.POST.get('password')
    user = Useraccount.objects.filter(username=username1).first()
    if result1 == 'login':
        if user is not None:
            if user.password == password1:
                results2 = '登录成功'
                print(results2)
                request.session['username'] = username1
                return redirect('/index/')
            else:
                results2 = '登录失败'
                print(results2)
                return render(request, 'login.html', {'results2': results2})
        else:
            results2 = '登录失败'
            print(results2)
            return render(request, 'login.html', {'results2': results2})
    else:
        return render(request, "register.html")
    
def register(request):
    username1=request.POST.get('username')
    password1=request.POST.get('password')
    if username1 != '':
        if password1 != '':
            if not Useraccount.objects.filter(username=username1).exists():
                user=Useraccount(username=username1,password=password1)
                user.save()
                result='注册成功'
                return render(request,"register.html",{'result':result})
            else:
                result='该用户名已存在'
                return render(request,"register.html",{'result':result})
        else:
            result='请输入账号与密码'
            return render(request,"register.html",{'result':result})
    else:
        result='请输入账号与密码'
        return render(request,"register.html",{'result':result})

def userinf(request):
    username = request.session.get('username')
    result=Useraccount.objects.filter(username=username)
    return render(request,"userinformation.html", {'result':result})

def resetandquit(request):
    name1=request.POST.get('button')
    print(name1)
    if name1 == 'resetname':
        chaxun1=request.POST.get('chaxun')
        chaxun=Useraccount.objects.get(username=chaxun1)
        appname=request.POST.get('name')
        chaxun.appname= appname
        chaxun.save()
        result=Useraccount.objects.filter(username=chaxun1)
        return render(request,"resetname.html",{"result":result})
    if name1 == 'quit':
        request.session.flush()
        return redirect('/useraccount/')
    if name1 == 'chongzhi':
        return render(request,'chongzhi.html')
