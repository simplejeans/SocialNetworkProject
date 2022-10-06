
from django.utils import timezone


class AccountLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user.is_authenticated:
            user.last_request = timezone.now()
            user.save()
        return self.get_response(request)
