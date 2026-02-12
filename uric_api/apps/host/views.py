from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers
# Create your views here.
class HostCategoryApiView(ModelViewSet):
	queryset = models.HostCategory.objects.filter(is_deleted=False).order_by("-id")
	serializer_class = serializers.HostCategorySerializer
	# permission_classes = [IsAuthenticated]
	
class HostApiView(ModelViewSet):
	queryset = models.Host.objects.filter(is_deleted=False).order_by("-id")
	serializer_class = serializers.HostSerializer
	# permission_classes = [IsAuthenticated]