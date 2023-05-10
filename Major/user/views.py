from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def account(request):
    profile=request.user.profile
    context={
        'profile':profile,

    }
    return render(request,'user/account.html',context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username=request.POST['username'].lower()
        password=request.POST['password']
        try:
            user=User.objects.get(username=username)
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                print('login successfully')
                return redirect(request.GET['next'] if 'next' in request.GET else 'account')
            else:
                print('Username OR password is incorrect')
        except:
            print('Username does not exist')
    return render(request,'user/login.html')

@login_required(login_url='login') 
def logoutUser(request):
    logout(request)
    print('logOut Successfully')
    return redirect('login')

def signup(request):
    return render(request,'user/signup.html')