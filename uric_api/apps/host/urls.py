from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('host', views.HostApiView, basename='host')
router.register('category', views.HostCategoryApiView, basename='category')


urlpatterns = [

] + router.urls