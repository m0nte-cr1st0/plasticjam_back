from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

from .views import UsersAPIView


router = SimpleRouter()
router.register(r'', UsersAPIView, basename='users')

urlpatterns = [
    url(r'', include(router.urls)),
]
