"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^$', 'django.contrib.auth.views.login',
            {'template_name': 'index.html'}, name='url_login'),

    url(r'^registrar$', 'project.views.register', name='register'),
    #url(r'^accounts/profile/$', 'PlayEnglish.views.home_barra',
    #   name='url_home_barra'),

    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'index.html'}, name='url_logout'),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'index.html'}, name='url_login'),

    url(r'^admin/', include(admin.site.urls)),
]
