from django.urls import path
from . import views

urlpatterns = [
    # DictType URLs
    path('types/', views.DictTypeList.as_view(), name='dict-type-list'),
]