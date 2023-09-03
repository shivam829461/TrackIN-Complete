"""trackin URL Configuration

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
from django.urls import path
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="home"),
    path("about/",views.about,name="about"),
    # path("<dyna>", views.dynamic),
    path("partner/", views.partner,name="partner"),
    path("track/", views.track,name="track"),
    path("ship/", views.ship,name="ship"),
    path("services/", views.services,name="services"),
    path("shipwithus/", views.shipwithus,name="shipform"),
    path("postage/", views.get_cities, name="postage"),
    path("locateus/", views.mapdetails,name="map"),
    
]
