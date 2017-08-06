"""personal_page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.aindex, name='home'),
    url(r'^index.html/$', views.aindex, name='index'),
    url(r'^about.html/$', views.about, name='about'),
    url(r'^blog.html/$', views.blog, name='blog'),
    url(r'^contact.html/$', views.contact, name='contact'),
    url(r'^portfolio.html/$', views.portfolio, name='portfolio'),
    url(r'^services.html/$', views.services, name='services'),
    url(r'^sendemail.html/$', views.sendemail, name='sendemail'),
]
