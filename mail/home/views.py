from django.shortcuts import render,redirect
from django.http.response import HttpResponse

from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def index(request):
   return render(request,'index.html')

def home(request):
   return render(request,'home.html')


def ho(request):
    if request.method=='POST':
        subject = request.POST['sub']
        message = request.POST['msg']
        email_from = settings.EMAIL_HOST_USER
        to = request.POST['to']
        recipient_list = [to,]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('/home/')