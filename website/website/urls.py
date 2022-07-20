"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from webpages.views import list_jobs, retrieve_jobs, listing_create,listing_update, listing_delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webpages.urls')),
    path('jobs', list_jobs),
    path('job/<pk>/', retrieve_jobs),
    path('forms/', listing_create),
    path('job/<pk>/edit/', listing_update),
    path('job/<pk>/delete/', listing_delete)
]
