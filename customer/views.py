from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'customer/login.html')

def register(request):
    if(request.method=="GET"):
        return render(request,'customer/register.html')