from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
#from django.http import HttpResponse
# Create your views here.
from .models import Room
# rooms=[
#     {'id':1, 'name': 'let\'s learn python'},
#     {'id':2, 'name': 'another one'},
#     {'id':3, 'name': 'front end developers'},
# ]
def loginPage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method =='POST':
        username  = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user= User.objects.get(username= username)
        except:
            messages.error(request, 'user does not exist')
        user = authenticate(request, username= username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'base/dashboard.html')
        else:
            messages.error(request, "username or password does not exist")
    context= {'page':page}
    return render(request , 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
        
        # page='register'
        form= UserCreationForm()
        if request.method =='POST':
            form= UserCreationForm(request.POST)
            if form.is_valid():
                user= form.save(commit=False)
                user.username=user.username.lower()
                user.save()
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "an error occured during registration")
        return render(request, 'base/login_register.html', {'form':form})
def home(request): 
    rooms =Room.objects.all() 
    context={'rooms': rooms}
    return render(request, 'base/home.html',context)

def room(request,pk):
    room= Room.objects.get(id=pk)
    


    context={'room':room}
    return render(request, 'base/room.html', context)
def astronomy_club(request):
    return render(request, 'base/astronomy_club.html')

#after this is trial

# your_app/views.py
# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from django.views import View
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# class SignUpView(View):
#     def get(self, request):
#         form = UserCreationForm()
#         return render(request, 'signup.html', {'form': form})

#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#         return render(request, 'signup.html', {'form': form})

# class LoginView(View):
#     def get(self, request):
#         form = AuthenticationForm()
#         return render(request, 'login.html', {'form': form})

#     def post(self, request):
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('dashboard')
#         return render(request, 'login.html', {'form': form})

# class DashboardView(View):
#     def get(self, request):
#         # Add logic for displaying user dashboard
#         return render(request, 'dashboard.html')
