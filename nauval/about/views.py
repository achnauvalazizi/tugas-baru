from django.shortcuts import render

# Create your views here.

def index(request):
    context ={
        'judul':'ABOUT'
    }
    return render(request,'about/index.html',context)