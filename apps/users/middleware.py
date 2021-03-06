from urllib.parse import urlparse

from django.conf import settings
from django.core.urlresolvers import resolve

from corsheaders.middleware import CorsMiddleware as BaseCorsMiddleware


class CorsMiddleware(BaseCorsMiddleware):
    """
    Override 'corsheaders.CorsMiddleware' for blocking own domain for url
    from CORS_BLOCKED_URLS list
    """
    def process_response(self, request, response):
        if request.META.get('HTTP_REFERER'):
            referrer_domain = current_domain = request.META['HTTP_HOST']
            referrer_path = urlparse(request.META['HTTP_REFERER'])
            referrer_port = referrer_path.port

            if referrer_port:
                referrer_domain = referrer_path.hostname + ':' + str(referrer_port)

            current_url = resolve(request.path_info)
            if current_url.url_name in settings.CORS_BLOCKED_URLS and referrer_domain != current_domain:
                return response

        return super().process_response(request, response)
