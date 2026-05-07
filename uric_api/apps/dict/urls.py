from django.urls import path
from . import views

urlpatterns = [
    # DictType URLs
    path('types/', views.DictTypeListCreateView.as_view(), name='dict-type-list'),
    path('types/<int:pk>/', views.DictTypeRetrieveUpdateDestroyView.as_view(), name='dict-type-detail'),
    
    # DictData URLs
    path('items/', views.DictDataListCreateView.as_view(), name='dict-data-list'),
    path('items/<int:pk>/', views.DictDataRetrieveUpdateDestroyView.as_view(), name='dict-data-detail'),
]