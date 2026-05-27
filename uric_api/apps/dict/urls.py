from django.urls import path
from . import views
from .views import DictTypeList, DictDataAPI

urlpatterns = [
    # DictType URLs
    path('types/', views.DictTypeList.as_view(), name='dict-type-list'),
    path('types/<int:pk>/', views.DictTypeList.as_view()),

    path('items/', views.DictDataAPI.as_view(), name='dict-item-list'),
    path('items/<int:pk>/', views.DictDataAPI.as_view()),

]