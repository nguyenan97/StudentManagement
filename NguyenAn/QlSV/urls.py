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
from django.conf.urls import url
from django.urls import include
from sys import path
from django.conf.urls import handler400,handler500
from QlSV import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
  #  path('admin/', admin.site.urls),

    url(r'^home/$',views.index ,name="home"),
    url(r'^detail/$',views.detail ,name="detail"),
    url(r'^gioiThieu/$', views.gioiThieu,name="gioiThieu"),
    url(r'^gioiThieu/(?P<maGV>[0-9]+)/$', views.teacherDetail, name="teacherDetail"),
    url(r'^sv/$',views.sv ,name="sv"),
    url(r'^login/$', views.login, name="login1"),
    url(r'^giangVien/$',views.giangVien,name="giangVien"),
    url(r'^GiangVien/$', views.loginGV, name="gv"),
   # url(r'^abc/$', views.listStudent, name="listST"),
]
handler404 = 'QlSV.views.error'
handler500 = 'QlSV.views.error'
