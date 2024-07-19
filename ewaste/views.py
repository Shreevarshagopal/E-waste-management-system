from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib import messages


# Create your views here.

def index(request):
    if 'mail'in request.session:
        context={
            'session':request.session['mail'],
        }
        print(context)
        return render(request,'index.html',context)
    return render(request,'index.html')

def registration(request):
    if request.method=='POST':
        username=request.POST.get('username')
        mobnum=request.POST.get('mobnum')
        mail=request.POST.get('mail')
        password=request.POST.get('password')
        repassword=request.POST.get('repassword')
        try:
            data=Registration.objects.get(mail=mail)
            context={'error':"Mail ID already Registered please try something else.."}
            return render (request,'register.html',context)
        except:
            if password==repassword:
                i=Registration()
                i.username=username
                i.mobnum=mobnum
                i.mail=mail
                i.password=password
                i.save()
                messages.success(request, 'Your Registration Successfull please login')
                return redirect('login')
            else:
                context={'error':"Password must be same..."}
                return render (request,'register.html',context)

    return render (request,'register.html')

def login(request):
    if request.method=='POST':
        mail=request.POST.get('mail')
        password=request.POST.get('password')
        try:
            data=Registration.objects.get(mail=mail)
            if data.password==password:
                request.session['mail']=mail   
                return redirect('index')
            else:
                messages.error(request, 'password Does not Match !!')
                return redirect('login')
        except:
            messages.error(request, 'No user found !!')
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    if 'mail'in request.session:
        del request.session['mail']
    return redirect('index')

def home(request):
    if 'mail' in request.session:
        data=Category.objects.all()
        context={
            'session':request.session['mail'],
            'data':data,
        }
        return render(request,'home.html',context)
    return redirect('index')
    
def category(request,id):
    if 'mail' in request.session:
        a=Category.objects.get(id=id)
        data=Total_cat.objects.all().filter(cat_name_id=a.id)
        for i in data:
            print(i.waste_name)
        context={
            'session':request.session['mail'],
            'data':data,
        }
        return render(request,'category.html',context)
    return redirect('index')

    