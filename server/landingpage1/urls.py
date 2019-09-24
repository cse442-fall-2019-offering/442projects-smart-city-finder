from django.contrib import admin
from django.conf.urls import url, include
from landingpage1.views import index
from django.urls import path


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', index),
]