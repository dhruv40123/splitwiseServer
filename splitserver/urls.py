
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from myserver.home import *

urlpatterns = [
    path('', index, name="home"),
    path('expense/', include('myserver.urls')),
    path('admin/', admin.site.urls),
]
