from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views
urlpatterns = [
	path("login/", TokenObtainPairView.as_view()),
	path("jwt/refresh/", TokenRefreshView.as_view()),
	path("jwt/verify/", TokenVerifyView.as_view()),
]