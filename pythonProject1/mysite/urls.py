
"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
<<<<<<< HEAD

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

import blog.views
=======
from django.urls import path, include
from django.urls import path
from django.conf.urls.static import static # импортировали из настроек статику
from django.conf import settings # импортировали из настроек свои записи

import home.views
>>>>>>> aa63bd7a62534e62ac69d41229e1af6264db648c

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home, name='home'),
    path('blog/', include('blog.urls'), name='blog'),
    path('sign/', include('regUser.urls')),

]
<<<<<<< HEAD
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> aa63bd7a62534e62ac69d41229e1af6264db648c
