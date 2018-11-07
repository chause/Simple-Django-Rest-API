"""MarvelAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from application import views

urlpatterns = [
    path(
        'admin/',
        admin.site.urls,
        name="admin"
    ),
    path(
        'hero/',
        views.HeroList.as_view(),
        name="hero_list"
    ),
    path(
        'hero/<int:id>/',
        views.HeroSelect.as_view(),
        name="hero_select"
    ),
    path(
        'hero/<int:id>/stats/',
        views.HeroStats.as_view(),
        name="hero_stats"
    ),
    path(
        'villain/',
        views.VillainList.as_view(),
        name="villain_list"
    ),
    path(
        'villain/<int:id>/',
        views.VillainSelect.as_view(),
        name="villain_select"
    ),
    path(
        'villain/<int:id>/stats/',
        views.VillainStats.as_view(),
        name="villain_stats"
    ),
]
