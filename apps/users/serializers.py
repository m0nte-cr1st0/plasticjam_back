from django.db.models import Sum, F

from rest_framework import serializers

from .models import User, Statistic


class UserListSerializer(serializers.ModelSerializer):
    total_clicks = serializers.SerializerMethodField()
    total_page_views = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'gender', 'ip_address',
            'total_clicks', 'total_page_views'
        ]

    def get_total_clicks(self, obj):
        return sum(obj.statistics.values_list('clicks', flat=True))

    def get_total_page_views(self, obj):
        return sum(obj.statistics.values_list('page_views', flat=True))


class DateRangeSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    # end_date = serializers.DateField()


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = ['date', 'clicks', 'page_views']


class UserStatisticSerializer(serializers.ModelSerializer):
    statistics = StatisticSerializer(many=True)

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'gender', 'ip_address', 'statistics',
                    ]

class UserDetailStatisticSerializer(serializers.Serializer):
    user = UserStatisticSerializer()
    date = DateRangeSerializer()
