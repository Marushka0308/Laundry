"""laundry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from laundry import sign_up_views
from laundry import login_views
from laundry import laundry_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', sign_up_views.sign_up),
    path('users/<int:id>',sign_up_views.sign_up_detail),
    path('login/', login_views.login, name='login'),
    path('laundry/', laundry_views.laundry),
    path('laundry/<int:id>',laundry_views.laundry_detail),
    path('laundry/upload',laundry_views.upload, name='upload')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)