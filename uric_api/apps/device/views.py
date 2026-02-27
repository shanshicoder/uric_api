from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import BrowsableAPIRenderer , JSONRenderer
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.views import APIView

from .models import DeviceModel , DeviceCateModel , DeviceAttrModel
from .serializers import DeviceAttrSerializer, DeviceSerializer, DeviceCateSerializer


class DeviceCateView(GenericAPIView):
	queryset = DeviceCateModel.objects.all()  # 告诉 DRF 数据从哪来
	serializer_class = DeviceCateSerializer
	
	parser_classes = [FormParser, MultiPartParser, JSONParser]
	renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
	
	def get(self, request, *args, **kwargs):
		queryset = self.get_queryset( )
		# self.get_serializer() 实例化序列化器
		serializer = self.get_serializer(queryset , many=True)
		return Response(serializer.data)
	
	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=False)  # 或者手动处理错误
		if not serializer.is_valid():
			return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
		serializer.save()
		return Response(serializer.data , status=status.HTTP_201_CREATED)

class DeviceAttrView(GenericAPIView):
	
	queryset = DeviceAttrModel.objects.all()  # 告诉 DRF 数据从哪来
	serializer_class = DeviceAttrSerializer
	parser_classes = [FormParser, MultiPartParser, JSONParser]
	
	def get(self, request):
		deviceAttr = DeviceAttrModel.objects.all()
		serializer = DeviceAttrSerializer(deviceAttr, many=True)
		return Response(serializer.data)
	
	def post(self, request):
		serializer = DeviceAttrSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
class DeviceListView(APIView):
	def get(self, request):
		devices = DeviceModel.objects.all()
		serializer = DeviceSerializer(devices, many=True)
		return Response(serializer.data)
	
	def post(self, request):
		serializer = DeviceSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
		
	