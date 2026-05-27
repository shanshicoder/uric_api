from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import DeviceSerializer


class DeviceMgnAPI(APIView):

	def post(self, request, *args, **kwargs):
		"""
			添加设备资产
		"""
		request_data = request.data
		print(request_data)


		serializer = DeviceSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)