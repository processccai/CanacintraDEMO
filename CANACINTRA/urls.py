"""
URL configuration for CANACINTRA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.home.home_view import Home
from api.Begin.begin_view import Login,Register,Logout,Success_register

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',Home.as_view(),name='home'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('register',Register.as_view(),name='register'),
    path('success_register',Success_register.as_view(),name='success_register'),


]
