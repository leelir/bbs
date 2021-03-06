"""bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^detail/(\d+)/$',views.bbs_detail),
    url(r'^sub_comment/$', views.sub_comment),
    url(r'^login/$', views.login),
    url(r'^login_check/$', views.login_check),
    url(r'^logout/$', views.logout),
    url(r'^bbs_pub/$', views.bbs_pub),
    url(r'^bbs_sub/$', views.bbs_sub),
    url(r'^category/(\d+)/$', views.category)
]
