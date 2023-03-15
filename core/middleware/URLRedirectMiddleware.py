from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class UrlRedirectMiddleware(MiddlewareMixin):

    def process_request(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('core:welcome-page'))
        return None
