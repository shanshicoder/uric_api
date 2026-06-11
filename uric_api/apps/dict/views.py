from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import DictTypeModel, DictDataModel
from .serializers import DictTypeSerializer, DictDataSerializer


class DictTypeList(APIView):

    """
        多条件查询字典类型及字典项目列表
    """
    def get(self, request, format=None):

        status = self.request.query_params.get('status')
        query_type_name = self.request.query_params.get('type_name')
        query_pk = self.request.query_params.get('id')
        search_val = request.GET.get('search','')

        print(f"status: {status}, type_name: {query_type_name}")

        queryset = DictTypeModel.objects.all()

        #   多搜索值查询
        if search_val:
            queryset = queryset.filter(
                Q(type_name__contains=search_val) | Q(type_code__contains=search_val)
            )
        if status:
            queryset = queryset.filter(status=status)
        if query_type_name:
            queryset = queryset.filter(type_name__contains=query_type_name)
        if query_pk:
            queryset = queryset.filter(id=query_pk)
        #   在这里直接打印原生 SQL
        print("====== 当前执行的 SQL ======")
        print(str(queryset.query))
        print("===========================")
        return Response(DictTypeSerializer(queryset, many=True).data)
    
    """
        添加字典类型
    """
    def post(self, request, format=None):
        serializer = DictTypeSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
        根据主键id查询并修改字典类型
    """
    def put(self, request, pk):
        try:
            dict_type = DictTypeModel.objects.get(pk=pk)
        except DictTypeModel.DoesNotExist:
            return Response({"error":"该字典类型不存在"},status=status.HTTP_404_NOT_FOUND)

        serializer = DictTypeSerializer(instance=dict_type, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DictDataAPI(APIView):

    def get(self, request, format=None):
        """
            根据字典类型id查询对应的字典项目
        """
        dict_type_id = self.request.query_params.get('type_id')
        try:
            dict_type = DictTypeModel.objects.filter(id=dict_type_id)
        except DictTypeModel.DoesNotExist:
            return Response({"error":"无法添加该字典类型"},status=status.HTTP_404_NOT_FOUND)

        items = DictDataModel.objects.filter(dict_type_id=dict_type_id)

        return Response(DictDataSerializer(items, many=True).data)

    def post(self, request, format=None):
        """
            添加字典项目
        """
        serializer = DictDataSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
            根据主键修改字典项目
        """
        try:
            dict_data_obj = DictDataModel.objects.get(pk=pk)
        except DictDataModel.DoesNotExist:
            return Response({"error": "该字典项目不存在"}, status=status.HTTP_404_NOT_FOUND)

        #partial 部分更新字段
        serializer = DictDataSerializer(instance=dict_data_obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)