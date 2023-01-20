from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='blog-index'),
    path('sign_up/', views.sign_up, name='blog-index'),
]
