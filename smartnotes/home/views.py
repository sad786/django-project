from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'home/welcome.html',{})

@login_required(login_url='/admin')
def authorized(req):
    return render(req,'home/authorized.html',{})
