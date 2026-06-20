from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from . models import Student,Product


def addstudentform(request):
    return render(request,'add-student.html')

def addstudentformprocess(request):
    txt1 = request.POST['txt1']
    txt2 = request.POST['txt2']
    txt3 = request.POST['txt3']
    txt4 = request.POST['txt4']
    Student.objects.create(name=txt1,mobile=txt2,email=txt3,address=txt4)
    return HttpResponse("Thank you")


def displayStudent(request):
    mystudentlist = Student.objects.all()
    return render(request,'display-student.html',{'mydata':mystudentlist})

def displayProduct(request):
    productList = Product.objects.all()
    return render(request,'product.html',{'mydata':productList})

def displayProductApi(request):
    product_list = Product.objects.all().values('id', 'title', 'price','image','category','details')
    
    # Convert the QuerySet into a standard Python list
    data = list(product_list)
    
    # safe=False is mandatory because data is a List [], not a Dict {}
    return JsonResponse(data, safe=False)

def deleteStudent(request,id):
    Student.objects.get(id=id).delete()
    return redirect(displayStudent)

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




def user_register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Registration Successful")
        return redirect('login')

    return render(request, 'user_register.html')


def user_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, 'user_login.html')


def user_home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'user_home.html')


def user_logout_view(request):
    logout(request)
    return redirect('login')
