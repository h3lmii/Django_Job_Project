from django.contrib import admin
from django.urls import path,include
from .views import index,Home,ApplyPage

urlpatterns = [
    path('',index ,name='homepage'),

    path('dashboard/',Home.as_view() ,name='dashboard'),
    path('apply/',ApplyPage.as_view(),name='apply'),


    


    
]
