import datetime
from typing import Iterable, Union

from rest_framework import filters, serializers

from .models import User, Statistic


StatisticQueryset = Union['QuerySet', Iterable['Statistic']]


class UserStatisticFilter(filters.BaseFilterBackend):
    """
    Filters Statistic queryset by user, start_date and end_date params
    """
    def filter_queryset(self, request, queryset, view) -> StatisticQueryset:
        params = request.query_params

        pk = params.get('user_pk')

        # For testing url `/api/v1/users/<id>`
        if not pk:
            pk = request.path.split('/')[-2]

        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise serializers.ValidationError('User not found')
        last_date = user.statistics.only('date').last().date
        start_date = request.query_params.get('start_date', last_date - datetime.timedelta(days=6))
        end_date = request.query_params.get('end_date', last_date)
        if not end_date:
            end_date = last_date
        if isinstance(start_date, str):
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        if isinstance(end_date, str):
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        if start_date > end_date:
            start_date, end_date = end_date, start_date
        queryset = Statistic.objects.filter(user=user, date__gte=start_date, date__lte=end_date)
        return queryset
