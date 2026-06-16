from . import views
from django.urls import path

urlpatterns = [
    path('',views.homepage),
    path('home',views.homepage),
    path('about',views.aboutpage),    
    path('contact',views.contactpage), 
    path('cake',views.contactpage), 
    path('cake/ahmedabad',views.contactpage), 
    path('cake/rajkot',views.contactpage),    
    
]