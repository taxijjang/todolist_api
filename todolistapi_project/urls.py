from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from todolistapi import views
router = DefaultRouter()
router.register('dolistapi', views.DoListViewSet)
router.register('donelistapi',views.DoneListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
