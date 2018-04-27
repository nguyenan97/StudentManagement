"""NguyenAn URL Configuration

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
from django.conf.urls import include,url
from django.contrib import admin
from django.urls import path
from QlSV import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'',include('QlSV.urls')),
    #url(r'home/$',views.index,name ="index" ),
    #url(r'^home/',include('QlSV.urls')),
   #url(r'^svd/',include('QlSV.urls')),
   # url(r'^sv/',include('QlSV.urls')),
    #url(r'^sv1/',include('QlSV.urls')),
   #url(r'^gv/',include('QlSV.urls')),
    #url(r'^login/',include('QlSV.urls')),


    #url('',views.index),

    #url(r'gioiThieu/$', views.gioiThieu),
  #  url(r'^(?P<maGV>[0-9]+)/$', views.teacherDetail, name="teacherDetail"),

    #url(r'sv/$',views.sv,name="sv" ),
    #url(r'login/$',views.Login, ),
    #url(r'^(?P<maSV>[0-9]+)/$', views., name="teacgerDetail"),
    #url(r'^(?P<maSV>[0-9]+)/$',views.detail, name="detail" ),
    #url(r'giangVien/$',views.giangVien),




]
handler404 = 'QlSV.views.error'
handler500 = 'QlSV.views.error'
