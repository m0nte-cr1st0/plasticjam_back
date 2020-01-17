from rest_framework.generics import ListAPIView

from .filters import UserStatisticFilter
from .models import User, Statistic
from .pagination import UsersSetPagination
from .serializers import UserSerializer, StatisticSerializer


class UserListApiView(ListAPIView):
    """
    list:
    Users list

    Return list of users from database using custom pagination
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = UsersSetPagination


class StatisticAPIView(ListAPIView):
    """
    list:
    Statistics for user and their data

    Return list of user statistics using custom filtering
    """
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer
    filter_backends = [UserStatisticFilter]
