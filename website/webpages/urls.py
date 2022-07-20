from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
    # path('jobs', views.list_jobs, name='list_jobs')
]