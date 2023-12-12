"""
URL configuration for pidjango project.

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
from django.urls import path
from playground import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('file_selection/', views.file_selection, name='file_selection'),
    #path('read_file/<int:file_id>/', views.read_file, name='read_file'),
    path('',views.index),
    path('file', views.file_list, name='file_list'),#File
    path('file/add', views.add_file, name='add_file'),#File
    path('file/<int:pk>/remove', views.remove_file, name='remove_file'),#File
    path('file/<int:pk>/edit', views.edit_file, name='edit_file'),#File
    path('file/<int:pk>/play',views.play_file, name='play_file'),#File
    path('file/succesful_upload', views.succesful_upload, name='succesful_upload')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
