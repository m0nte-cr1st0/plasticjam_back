import datetime
from typing import Iterable, Union

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import User, Statistic
from .serializers import UserListSerializer, UserStatisticSerializer, StatisticSerializer


class UsersSetPagination(PageNumberPagination):
    page_size_query_param = 'users_count'


class UserListApiView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    pagination_class = UsersSetPagination


class UserStatisticApiView(RetrieveAPIView):
    """
    retrieve:
    Users detail statistic

    Get dates range for statistic
    """

    StatisticQueryset = Union['QuerySet', Iterable['Statistic']]

    serializer_class = UserStatisticSerializer
    statistic_serializer_class = StatisticSerializer
    queryset = User.objects.all()

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        user_serializer = self.get_serializer(user)
        statistics = self.get_statistics(user)
        statistics_serializer = self.statistic_serializer_class(statistics, many=True)
        dates = user.statistics.only('date')
        min_date = dates.first().date
        max_date = dates.last().date
        return Response({
            'user_data': user_serializer.data,
            'statistics': statistics_serializer.data,
            'dates_rang': [min_date, max_date]
        })

    def get_statistics(self, user: User) -> StatisticQueryset:
        last_date = user.statistics.only('date').last().date
        start_date = self.request.query_params.get('start_date', last_date - datetime.timedelta(days=6))
        end_date = self.request.query_params.get('end_date', last_date)
        if start_date > end_date:
            start_date, end_date = end_date, start_date
        queryset = Statistic.objects.filter(user=user, date__gte=start_date, date__lte=end_date)
        return queryset
