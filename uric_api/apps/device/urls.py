from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('deviceCate/' , views.DeviceCateView.as_view( ) , name='devicecate-list-create') ,
    path('deviceAttr/', views.DeviceAttrView.as_view()),
]

