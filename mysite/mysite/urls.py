"""mysite URL Configuration

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
# import  sys
# import imp
# import django
# sys.path.insert(0,'E:\\djcode\\mysite')
# imp.reload(django)
from django.conf.urls import url,include
from django.contrib import admin
from views import hello,current_datetime,hours_ahead,view1,view2,showpic,showcsv,show_color,set_color,login_after_view,register

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^book/',include('books.urls')),
    url(r'view1/$',view1),
    url(r'view2/$',view2),
    url(r'showpic/',showpic),
    url(r'showcsv/',showcsv),
    url(r'showcolor/',show_color),
    url(r'setcolor/',set_color),
    url(r'loginafter',login_after_view),
    url(r'register',register),
]
