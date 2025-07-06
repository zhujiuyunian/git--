from django.shortcuts import render
from .models import Index
# Create your views here.
def index(request):
    results = Index.objects.all()
    return render (request,"index.html",{"results":results})

def search(request):
    results=request.POST.get('search')
    name1=Index.objects.filter(name= results)
    return render(request,'index2.html',{'results':name1})