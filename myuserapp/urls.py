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
    path('logout',views.logout)
]