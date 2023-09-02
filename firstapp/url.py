from django.urls import path
from . import views

urlpatterns=[
    path('Home',views.Home,name='Number finder'),
    path('upload/', views.upload, name='upload'),
    path('download_data', views.download_data, name='upload1'),
]