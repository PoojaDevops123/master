import os
from django.conf import settings
from summary.models import User_Model
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':

        try:
            userDeat = User_Model.objects.get(user_UserName=request.POST.get(
                'login_UserName'), user_PWD=request.POST.get('login_PWD'))
            request.session['UserName'] = userDeat.user_UserName
            return HttpResponseRedirect('summary_dash')

        except User_Model.DoesNotExist:
            context = {
                'err': "Check Credentials"
            }
        return render(request, 'pages/login.html', context)
    if request.method == 'GET':
        if request.session.get('UserName') is None:
            logged_suc = request.GET.get('logout')
            context = {
                'logged_suc': logged_suc
            }
            return render(request, 'pages/login.html', context=context)
        else:
            return HttpResponseRedirect('summary_dash')


def log_out(request):
    request.session['UserName'] = None
    return HttpResponseRedirect('login?logout=suc')
