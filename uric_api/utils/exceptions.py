import logging

from django.db import DatabaseError
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework import status

logger = logging.getLogger('django')
def custom_exception_handler(exc, context):
	"""
		自定义异常处理
	"""
	
	response = exception_handler(exc, context)
	
	if response is None:
		view = context["view"]
		if isinstance(exc, DatabaseError):
			logger.error('[%s] %s' % (view,exc))
			response = Response({'errmsg': '服务器内部错误'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
		
	return response