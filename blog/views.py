from django.shortcuts import render
from .models import Blog
# Create your views here.
def index(request):
    data = Blog.objects.all()
    return render(request,'index.html',{'blog':data})

def detail(request,id):
    data = Blog.objects.get(id=id)
    print(data)
    return render(request,'single.html',{'data':data})
