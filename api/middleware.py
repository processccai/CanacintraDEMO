# tuapp/middleware.py

from django.utils import timezone

class SessionRenewalMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            request.session['last_activity'] = timezone.now().timestamp()

        response = self.get_response(request)
        return response
