from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('device/', views.DeviceMgnAPI.as_view(), name='device_mng_api'),
    path('attr/', views.DeviceAttrAPI.as_view(), name='attr_mng_api'),
]

