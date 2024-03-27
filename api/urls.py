from django.contrib import admin
from django.urls import path
from api import views

from rest_framework import routers

from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('message/', views.msg), 
    path('api-token-auth/', obtain_auth_token)
]