"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

from .api.views import index_view, MessageViewSet

from .api.views import ListTodo, DetailTodo



router = routers.DefaultRouter()
router.register('messages', MessageViewSet)

urlpatterns = [

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/admin/
    path('admin/', admin.site.urls),

    path('api/v1/<int:pk>/', DetailTodo.as_view()),
    path('api/v1/', ListTodo.as_view())

]


