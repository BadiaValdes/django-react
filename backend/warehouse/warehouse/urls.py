"""warehouse URL Configuration

The `urlpatterns` list routes URLs to auxView. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function auxView
    1. Add an import:  from my_app import auxView
    2. Add a URL to urlpatterns:  path('', auxView.home, name='home')
Class-based auxView
    1. Add an import:  from other_app.auxView import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('warehouseApp.url'))
]

# Añadir archivos estáticos a la url
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
