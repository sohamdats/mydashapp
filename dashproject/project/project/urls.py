"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from myapp import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^full_list/$',views.full_list,name='full_list'),
    url(r'^detail_page/(?P<ts>(([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]))/$',views.detail_page,name='detail_page'),
    url(r'^detail_page/(?P<ts>(([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]))/(?P<name>([a-z]*_[a-z]*))/$',views.usage_detail_page,name='udp'),
    url(r'^detail_page/(?P<ts>(([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]))/(?P<name>([a-z]*_[a-z]*))/(?P<usage>(cpu_usage|memory_usage))',views.usage_detail_page,name='u'),
]
