from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateNewList
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='account/login')
def home(response):
    return render(response, 'main/home.html', {})

@login_required(login_url='account/login')
def category(response):
    return render(response, 'main/category.html', {})

@login_required(login_url='account/login')
def about(response):
    return render(response, 'main/about.html', {})

@login_required(login_url='account/login')
def profile(response):
    currentuser = response.user
    userprofile = User.objects.filter(username=currentuser.username)
    return render(response, 'main/profile.html', {'profile':userprofile})

@login_required(login_url='account/login')
def phishing(response):
    return render(response, 'main/phishing.html', {})

@login_required(login_url='laccount/login')
def ddos(response):
    return render(response, 'main/ddos.html', {})

@login_required(login_url='account/login')
def mitm(response):
    return render(response, 'main/mitm.html', {})

@login_required(login_url='account/login')
def bruteforce(response):
    return render(response, 'main/bruteforce.html', {})

@login_required(login_url='account/login')
def packetsniffing(response):
    return render(response, 'main/packetsniffing.html', {})

@login_required(login_url='account/login')
def zphisher(response):
    return render(response, 'main/zphisher.html', {})
    
@login_required(login_url='account/login')
def socialphish(response):
    return render(response, 'main/socialphish.html', {})

@login_required(login_url='account/login')
def LOIC(response):
    return render(response, 'main/LOIC.html', {})

@login_required(login_url='account/login')
def slowloris(response):
    return render(response, 'main/slowloris.html', {})

@login_required(login_url='account/login')
def ettercap(response):
    return render(response, 'main/ettercap.html', {})

@login_required(login_url='account/login')
def xerosploit(response):
    return render(response, 'main/xerosploit.html', {})

@login_required(login_url='account/login')
def john(response):
    return render(response, 'main/john.html', {})

@login_required(login_url='account/login')
def aircrack(response):
    return render(response, 'main/aircrack.html', {})

@login_required(login_url='account/login')
def wireshark(response):
    return render(response, 'main/wireshark.html', {})

@login_required(login_url='account/login')
def tcpdump(response):
    return render(response, 'main/tcpdump.html', {})

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                messages.warning(request, 'Your account expires in three days.')
                messages.error(request, 'Document deleted.')

                return redirect ("/account/login/")

        context = {'form':form}
        return render(request, 'main/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/home/')
            else:
                messages.info(request, 'Username OR Password is incorrect.')

        context = {}
        return render(request, 'main/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/account/login')