from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import DeviceAttrModel
from .serializers import DeviceSerializer, DeviceAttrSerializer


class DeviceAttrAPI(APIView):
	def post(self, request):
		"""
			新增设备属性
		"""
		serializer = DeviceAttrSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request):
		"""
			获取树形结构属性列表
		"""
		attr_list = DeviceAttrModel.objects.all()
		serializer = DeviceAttrSerializer(attr_list,many=True)

		tree_data = build_tree(serializer.data)
		return Response(tree_data, status=status.HTTP_200_OK)

def build_tree(attr_list):
	print(attr_list)
	node_map = {}
	for item in attr_list:
		item['children'] = []
		node_map[item['id']] = item
	print(node_map)

	tree = []
	for item in attr_list:
		p_attr = item['p_attr']
		if p_attr == 0 or p_attr is None:
			tree.append(item)
		else:
			parent = node_map.get(p_attr)
			if parent is not None:
				parent['children'].append(item)
	return tree


class DeviceMgnAPI(APIView):

	def post(self, request, *args, **kwargs):
		"""
			添加设备资产
		"""
		serializer = DeviceSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)