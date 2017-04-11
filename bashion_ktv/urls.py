"""bashion_ktv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from customer.views import index_customer
from counter.views import index_counter
from website.views import index_website

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^counter/',counter.urls),
    url(r'^customer/index/$', index_customer, name='index_customer'),
    url(r'^counter/index/$', index_counter, name='index_counter'),
    url(r'^website/index/$', index_website, name='index_website'),
]
