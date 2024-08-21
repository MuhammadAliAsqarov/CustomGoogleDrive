from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
from .models import UserTracking
from django.utils.timezone import now


class RateLimitMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user_ip = self.get_client_ip(request)
        cache_key = f'rate_limit_{user_ip}'
        request_count = cache.get(cache_key, 0)
        if request_count >= 30:
            return JsonResponse({'error': 'Too Many Requests'}, status=429)
        if request_count == 0:
            cache.set(cache_key, 1, timeout=10)
        else:
            cache.incr(cache_key)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class UserTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.track_user(request)
        response = self.get_response(request)
        return response

    def track_user(self, request):
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None

        ip_address = self.get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
        path = request.path

        UserTracking.objects.create(
            user=user,
            ip_address=ip_address,
            user_agent=user_agent,
            path=path,
            timestamp=now()
        )

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
