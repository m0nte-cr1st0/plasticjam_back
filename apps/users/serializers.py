from rest_framework import serializers

from .models import User, Statistic


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
        return sum(obj.statistics.values_list('clicks', flat=True))

    def get_total_page_views(self, obj):
        return sum(obj.statistics.values_list('page_views', flat=True))


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = '__all__'

    def to_representation(self, instance):
        """
        Customizing output json data

        Adds extra fields to json, changes ``user`` field
        """
        output = super(StatisticSerializer, self).to_representation(instance)
        user = User.objects.get(pk=output['user'])
        user_serializer = UserSerializer(user)
        dates = user.statistics.only('date')
        output['user'] = user_serializer.data
        output['min_date'] = dates.first().date
        output['max_date'] = dates.last().date
        return output
