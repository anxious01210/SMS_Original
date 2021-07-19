from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from sm_app.EmailBackEnd import EmailBackEnd

# Create your views here.


def ShowDemoPage(request):
    return render(request, 'demo.html')


def ShowLoginPage(request):
    return render(request, 'sm_app/login_page.html')


def DoLogin(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Method is not allowed.</h2>')
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return HttpResponse('Email: ' + request.POST.get('email') + ' Password: ' + request.POST.get('password'))
        else:
            return HttpResponse('Invalid Login!')


def GetUserDetails(request):
    if request.user is not None:
        return HttpResponse('User: ' + request.user.email + ' user_type: ' + request.user.user_type)
    else:
        return HttpResponse('Please Login First')


def LogoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')

