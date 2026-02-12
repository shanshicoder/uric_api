import logging
import time
from django.utils.deprecation import MiddlewareMixin
from rest_framework import response

logger = logging.getLogger("django")


class LoggingMiddleware(MiddlewareMixin):
	"""配置日志记录耗时中间件"""
	start = 0
	def process_request(self, request):
		self.start = time.time()
		
	def process_response(self, request, response):
		cost_timer = time.time()-self.start
		
		if cost_timer > 0.01:
			logger.warning(f"请求路径{request.path} 耗时 {cost_timer}秒")
		
		return response

class CorsMiddleware(MiddlewareMixin):
	"""
		跨域中间件
	"""
	def process_response(self, request,response):
		response["Access-Control-Allow-Origin"] = "*"
		if request.method == "OPTIONS":
			response["Access-Control-Allow-Headers"] = "Content-Type"
			response["Access-Control-Allow-Methods"] = "PUT,PATCH,DELETE"
		return response