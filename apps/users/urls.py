from django.conf.urls import url, url

from .views import UserListApiView, UserStatisticApiView

urlpatterns = [
    url(r'^$', UserListApiView.as_view()),
    url(r'^(?P<pk>\d+)/$', UserStatisticApiView.as_view()),
]
