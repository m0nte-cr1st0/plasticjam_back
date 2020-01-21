from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import User
from .pagination import UsersSetPagination
from .serializers import UserSerializer, UserStatisticSerializer


class UserListApiView(ListAPIView):
    """
    list:
    Users list

    Return list of users from database using custom pagination
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = UsersSetPagination


class StatisticAPIView(RetrieveAPIView):
    """
    retrieve:
    Statistics for user and their data

    Return list of user statistics using custom filtering
    """
    serializer_class = UserStatisticSerializer
    queryset = User.objects.all()
