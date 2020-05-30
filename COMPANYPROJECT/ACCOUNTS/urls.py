from django.urls import path
from . import views

urlpatterns = [
    path('REGISTER', views.REGISTER,name='REGISTER'),

    path('upload',views.upload,name='upload'),

    path('painting', views.upload,name='painting'),

    path('rules', views.rules, name='rules'),

    path('rules1', views.rules1, name='rules1'),
]
