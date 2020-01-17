import datetime
from typing import Iterable, Union

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import filters, serializers

from .models import User, Statistic


StatisticQueryset = Union['QuerySet', Iterable['Statistic']]


class UserStatisticFilter(filters.BaseFilterBackend):
    """
    Filters Statistic queryset by user, start_date and end_date params
    """
    def filter_queryset(self, request, queryset, view) -> StatisticQueryset:
        params = request.query_params
        try:
            user = User.objects.get(pk=params['user_pk'])
        except UserDoesNotExist:
            raise serializers.ValidationError('User not found')
        last_date = user.statistics.only('date').last().date
        start_date = request.query_params.get('start_date',
            last_date - datetime.timedelta(days=6))
        end_date = request.query_params.get('end_date', last_date)
        if start_date > end_date:
            start_date, end_date = end_date, start_date
        queryset = Statistic.objects.filter(user=user, date__gte=start_date,
            date__lte=end_date)
        return queryset
