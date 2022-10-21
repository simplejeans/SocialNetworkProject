
from django.utils import timezone

from users.models import UserActivity


class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user.is_authenticated:
            user_activity = UserActivity.objects.update_or_create(user=request.user, defaults={"last_request": timezone.now()})
        return self.get_response(request)
