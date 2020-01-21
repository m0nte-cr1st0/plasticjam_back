import datetime
from typing import Iterable, Tuple

from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from .models import User, Statistic


Date = datetime.date
Dates = Iterable[Tuple[Date, Date]]


class UserSerializer(serializers.ModelSerializer):
    total_clicks = serializers.SerializerMethodField()
    total_page_views = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'email', 'gender', 'ip_address',
            'total_clicks', 'total_page_views'
        ]

    def get_total_clicks(self, obj):
        """
        Return total clicks count for every user
        """
        return sum(obj.statistics.values_list('clicks', flat=True))

    def get_total_page_views(self, obj):
        """
        Return total page views count for every user
        """
        return sum(obj.statistics.values_list('page_views', flat=True))


class UserStatisticSerializer(serializers.Serializer):
    user = serializers.SerializerMethodField()
    max_date = serializers.SerializerMethodField()
    min_date = serializers.SerializerMethodField()

    @swagger_serializer_method(serializer_or_field=UserSerializer())
    def get_user(self, obj):
        return UserSerializer(obj).data

    def get_max_date(self, obj):
        dates = obj.statistics.only('date')
        return dates.last().date

    def get_min_date(self, obj):
        dates = obj.statistics.only('date')
        return dates.first().date

    @staticmethod
    def get_dates(params: dict, obj: User) -> Dates:
        """
        Get dates for statistic from params
        """
        last_date = obj.statistics.only('date').last().date
        first_date = obj.statistics.only('date').first().date
        start_date = params.get('start_date', last_date - datetime.timedelta(days=6))
        end_date = params.get('end_date', last_date)
        if not end_date:
            end_date = last_date
        elif isinstance(end_date, str):
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        if not start_date:
            start_date = first_date
        elif isinstance(start_date, str):
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        if start_date > end_date:
            start_date, end_date = end_date, start_date
        return start_date, end_date

    @staticmethod
    def daterange(start_date: Date, end_date: Date):
        # https://stackoverflow.com/a/1060330/11214129
        for n in range(int ((end_date - start_date).days)):
            yield start_date + datetime.timedelta(n)

    def to_representation(self, instance):
        """
        Add statistic to output json
        """
        params = self.context['request'].query_params
        start_date, end_date = self.get_dates(params, instance)
        data = super().to_representation(instance)
        data['statistics'] = []
        for date in self.daterange(start_date, end_date):
            try:
                statistic = Statistic.objects.get(user=instance, date=date)
                clicks = statistic.clicks
                page_views = statistic.page_views
            except Statistic.DoesNotExist:
                clicks = page_views = 0
            data['statistics'].append(
                {'date': date, 'clicks': clicks, 'page_views': page_views}
            )
        return data


class StatisticSerializer(serializers.ModelSerializer):
    """
    Just for documentation
    """
    class Meta:
        model = Statistic
        fields = ['clicks', 'page_views', 'date']


class StatisticSwaggerSerializer(serializers.Serializer):
    """
    Just for documentation
    """
    user = UserSerializer()
    statistics = StatisticSerializer(many=True)
    max_date = serializers.DateField()
    min_date = serializers.DateField()
