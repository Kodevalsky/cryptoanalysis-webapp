"""
URL configuration for ZIT_Projekt project.

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
from core.views import homeView
from statistical.views import statisticalView
from bruteforce.views import bruteforceView, word_count_json_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  homeView.as_view() , name='home'),
    path('statistic/', statisticalView.as_view(), name='statisticalView'),
    path('bruteforce/', bruteforceView.as_view(), name='bruteforceView'),
    path('word-count-json/', word_count_json_view, name='word-count-json'),
    path('keypairs/', statisticalView.as_view(), name='keypairs')
]
