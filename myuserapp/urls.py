from . import views
from django.urls import path

urlpatterns = [
    path('',views.homepage),
    path('home',views.homepage),
    path('about',views.aboutpage),    
    path('contact',views.contactpage), 
    path('contactprocess',views.contactprocess), 
    path('cake',views.contactpage), 
    path('cake/ahmedabad',views.contactpage), 
    path('cake/rajkot',views.contactpage),    
    path('shop',views.shoppage),
    path('saveSession',views.saveSessionData),
    path('getSession',views.getSessionData),
    path('getSession2',views.getSessionData2),
    path('removeSession',views.deleteSessionData),
    
    path('login',views.loginpage),
    path('loginprocess',views.loginprocess),
    path('dashboard',views.dashboard),
    path('logout',views.logout),
        path('maildemo',views.mailsenddemo),
        path('add-student',views.addstudentform),
        path('add-student-process',views.addstudentformprocess),
        
        path('display-student',views.displayStudent),
        path('delete-student/<int:id>',views.deleteStudent),
         path('user_login', views.user_login_view, name='login'),
    path('user_register/', views.user_register_view, name='register'),
    path('user_home/', views.user_home_view, name='home'),
    path('user_logout/', views.user_logout_view, name='logout'),
    path('product/', views.displayProduct, name='product'),
        path('productapi/', views.displayProductApi, name='product'),


]