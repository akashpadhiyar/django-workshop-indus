from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def mailsenddemo(request):
    subject = 'Welcome to Facebook '
    message = ' You are Selected as CEO Position'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['akash@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("Mail Sent")


def homepage(request):
    return render(request,"home.html")
def aboutpage(request):
    return render(request,"about.html")

def shoppage(request):
    return render(request,'shop.html')

def contactpage(request):
    return render(request,"contact.html")

def saveSessionData(request):
    request.session.set_expiry(6)
    request.session['username'] = "Akash Padhiyar"
    return HttpResponse("Session Created")


def getSessionData(request):
    if request.session.has_key('username'):
        time  = request.session.get_expiry_age()
        print(time)
        msg = request.session['username']
        return HttpResponse(msg)
    else:
        return HttpResponse("Session Variable not Present ")

def deleteSessionData(request):
    del request.session['username'] 
    return HttpResponse("Session Removed")

def getSessionData2(request):
    msg = request.session['username']
    return HttpResponse(msg)

def contactprocess(request):
    a = int(request.POST['txt1'])
    b = int(request.POST['txt2'])
    c = a + b
    msg = "A Value is",a,"B Value is ",b,"Sum is ",c
    d = ""
    if c == 30:
        d = "If Condition Called"
    elif c<30:
        d = "Elseif Called"
    else:
        d= "Else Called"
    return render(request,'ans.html',{'mya':a,'myb':b,'myc':c,'myd':d})

def loginpage(request):
    return render(request,'login.html')
def loginprocess(request):
    txt1 = request.POST['email']
    request.session['myemail'] = txt1
    subject = 'Login Detected  '
    message = ' Someone has access you website Name is ',txt1
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['akash@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect(dashboard)

def dashboard(request):
    if request.session.has_key('myemail'):
        return render(request,"dashboard.html")
    else:
        return redirect(loginpage)
def logout(request):
    del request.session['myemail']
    return redirect(loginpage)