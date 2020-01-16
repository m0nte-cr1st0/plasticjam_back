"""plasticjam_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


api_patterns = [
    url(r'^api/v1/users/', include('apps.users.urls')),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += api_patterns

if settings.GENERATE_AUTO_DOCS:
    schema_view = get_schema_view(
        openapi.Info("PlasticJam", 'v1'),
        patterns=api_patterns,
        public=True,
    )

    urlpatterns += [
        url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
