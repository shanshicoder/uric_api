from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DictTypeModel
from .serializers import DictTypeSerializer


class DictTypeList(APIView):
    
    def get(self, request, format=None):
        """
        实现对电脑类型的多条件查询
        """
        queryset = DictTypeModel.objects.all()
       
        status = self.request.query_params.get('status')
        query_type_name = self.request.query_params.get('type_name')
        
        print(f"status: {status}, type_name: {query_type_name}")
        if status:
            queryset = queryset.filter(status=status)
        if query_type_name:
            queryset = queryset.filter(type_name__contains=query_type_name)
        
        # #   在这里直接打印原生 SQL
        # print("====== 当前执行的 SQL ======")
        # print(str(queryset.query))
        # print("===========================")
        return Response(DictTypeSerializer(queryset, many=True).data)
    
    
    def post(self, request, format=None):
        serializer = DictTypeSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

