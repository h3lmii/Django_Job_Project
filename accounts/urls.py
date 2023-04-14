from django.contrib import admin
from django.urls import path
from .views import SignUpPage,applyPage

urlpatterns = [
    path('signup/',SignUpPage.as_view(),name='signup'),
    path('apply/',applyPage,name='apply'),


]
