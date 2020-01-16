from django.conf.urls import url

from revproxy.views import ProxyView

from .views import UserListApiView, UserStatisticApiView

CORS_BLOCKED_URLS = [
    url(r'^(?P<pk>\d+)/', UserStatisticApiView.as_view(), name="user-detail"),
]

print(CORS_BLOCKED_URLS[0].name)
urlpatterns = [
    url(r'^$', UserListApiView.as_view(), name="users-list"),
]

urlpatterns += CORS_BLOCKED_URLS
