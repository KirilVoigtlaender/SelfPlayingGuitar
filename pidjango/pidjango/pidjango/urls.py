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
    path('admin/', admin.site.urls),#admin site
    path('delete',views.delete),#delete files
    path('delete/delete', views.delete_list, name='delete_list'),#delete Files
    path('delete/delete/<int:pk>/remove', views.remove_file, name='remove_file'),#delete Files
    path('edit',views.edit, name= 'edit'),#edit Files
    path('edit/edit', views.edit_list, name='edit_list'),#edit Files
    path('edit/edit/<int:pk>/edit', views.edit_file, name='edit_file'),#edit Files
    path('edit/edit/<int:pk>/form', views.edit_file, name='edit_form'),#edit files
    path('play',views.play),#play files
    path('play/play', views.play_list, name='play_list'),#play files
    path('play/play/<int:pk>/play',views.play_file, name='play_file'),#play files
    path('add/', views.add_file, name='add_file'),#add Files
    path('', views.website),#main page
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
