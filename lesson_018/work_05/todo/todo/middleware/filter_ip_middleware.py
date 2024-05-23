from django.core.exceptions import PermissionDenied

class FilterIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.META['REMOTE_ADDR'] != '127.0.0.1':
            raise PermissionDenied
        return self.get_response(request)