"""minitieba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from xiaotieba import views

urlpatterns = [
    path("",views.login,name="login"),
    path("register/",views.register,name="register"),
    path("admin/", admin.site.urls),
    path("xiaotieba/", include("xiaotieba.urls")),
    path("posts/", views.posts, name="posts"),
    path("postSearch/",views.postSearch,name="postSearch"),
    path("loginWork/", views.loginWork, name="loginWork"),
    path("register/registerWork/", views.registerWork, name="registerWork"),    
]
#设置静态文件路径
urlpatterns += staticfiles_urlpatterns()
print("++++staticfiles:",staticfiles_urlpatterns())
