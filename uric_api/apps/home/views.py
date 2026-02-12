from django.db import DatabaseError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
import logging
logger = logging.getLogger("django")

class HomeView(APIView):
	def get(self, request):
		logger.info("hello")
		return Response("Hello")
