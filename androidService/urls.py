"""androidService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include
from apps import *
from extra_apps import xadmin
from extra_apps.xadmin.plugins import xversion
from django.views import static
from django.conf.urls import url
from androidService.settings import MEDIA_ROOT

xversion.register_models()

xadmin.autodiscover()

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('', include('apps.login.urls', namespace='index')),
    path('service/', include('apps.service.urls', namespace='service')),
    url(r'^media/(?P<path>.*)$', static.serve, {"document_root": MEDIA_ROOT}, name='media'),
    path('ueditor/', include('DjangoUeditor.urls')),
]
