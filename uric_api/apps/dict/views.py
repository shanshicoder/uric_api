
from django.db.models import Q
from rest_framework import generics
from .models import DictTypeModel, DictDataModel
from .serializers import DictTypeSerializer, DictDataSerializer

# DictType views
class DictTypeListCreateView(generics.ListCreateAPIView):
    queryset = DictTypeModel.objects.all()
    serializer_class = DictTypeSerializer

    def get_queryset(self):
        """重写查询集，支持多参数过滤"""
        queryset = super().get_queryset()

        # 获取查询参数
        type_code = self.request.GET.get('type_code')
        type_name = self.request.GET.get('type_name')
        status_param = self.request.GET.get('status')
        is_show = self.request.GET.get('is_show')

        # 构建过滤条件
        filters = Q()

        if type_code:
            filters &= Q(type_code=type_code)

        if type_name:
            filters &= Q(type_name__icontains=type_name)

        if status_param is not None:
            # 将字符串转换为布尔值
            try:
                status_bool = status_param.lower() in ('true', '1', 'yes')
                filters &= Q(status=status_bool)
            except (ValueError, AttributeError):
                pass

        if is_show is not None:
            # 将字符串转换为布尔值
            try:
                is_show_bool = is_show.lower() in ('true', '1', 'yes')
                filters &= Q(is_show=is_show_bool)
            except (ValueError, AttributeError):
                pass

        # 应用过滤
        if filters:
            queryset = queryset.filter(filters)

        return queryset


class DictTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DictTypeModel.objects.all()
    serializer_class = DictTypeSerializer


# DictData views
class DictDataListCreateView(generics.ListCreateAPIView):
    queryset = DictDataModel.objects.all()
    serializer_class = DictDataSerializer

    def get_queryset(self):
        """重写查询集，支持多参数过滤"""
        queryset = super().get_queryset()

        # 获取查询参数
        dict_type_id = self.request.GET.get('type_id')
        label = self.request.GET.get('label')
        value = self.request.GET.get('value')
        status_param = self.request.GET.get('status')
        is_show = self.request.GET.get('is_show')

        # 构建过滤条件
        filters = Q()

        if dict_type_id:
            try:
                dict_type_id_int = int(dict_type_id)
                filters &= Q(dict_type_id=dict_type_id_int)
            except ValueError:
                pass

        if label:
            filters &= Q(label__icontains=label)

        if value:
            filters &= Q(value__icontains=value)

        if status_param is not None:
            # 将字符串转换为布尔值
            try:
                status_bool = status_param.lower() in ('true', '1', 'yes')
                filters &= Q(status=status_bool)
            except (ValueError, AttributeError):
                pass

        if is_show is not None:
            # 将字符串转换为布尔值
            try:
                is_show_bool = is_show.lower() in ('true', '1', 'yes')
                filters &= Q(is_show=is_show_bool)
            except (ValueError, AttributeError):
                pass

        # 应用过滤
        if filters:
            queryset = queryset.filter(filters)

        return queryset


class DictDataRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DictDataModel.objects.all()
    serializer_class = DictDataSerializer




