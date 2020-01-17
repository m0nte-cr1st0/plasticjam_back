from django.conf.urls import url

from .views import UserListApiView, StatisticAPIView


CORS_BLOCKED_URLS = [
    url(r'^(?P<pk>\d+)/', StatisticAPIView.as_view(), name="user-detail"),
]

urlpatterns = [
    url(r'^$', UserListApiView.as_view(), name="users-list"),
]

urlpatterns += CORS_BLOCKED_URLS
