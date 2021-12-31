from django.middleware.common import CommonMiddleware


class MiddlewareMixin:
    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        response = response or self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class CORSMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        # 添加响应头
        response["Access-Control-Allow-Origin"] = "*"

        # 允许携带Content-Type请求头
        # response["Access-Control-Allow-Headers"] = "Content-Type"

        # 允许请求的方法
        # response["Access-Control-Allow-Methods"] = "DELETE,PUT,POST"

        return response
