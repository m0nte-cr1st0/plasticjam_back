from django.utils.decorators import method_decorator
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import User
from .pagination import UsersSetPagination
from .serializers import UserSerializer, UserStatisticSerializer, StatisticSwaggerSerializer


@method_decorator(swagger_auto_schema(
    manual_parameters=[
        openapi.Parameter(
            name='start_date', in_=openapi.IN_QUERY, type='str',
            description='Start date for filter'
        ),
        openapi.Parameter(
            name='end_date', in_=openapi.IN_QUERY, type='str',
            description='End date for filter'
        )
    ],
    responses={'200': StatisticSwaggerSerializer}), name='retrieve'
)
class UsersAPIView(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    """
    list:
    Users list

    Return list of users from database using custom pagination

    retrieve:
    Statistics for user and their data

    Return list of user statistics for drawing chart
    """
    queryset = User.objects.all()
    pagination_class = UsersSetPagination

    def get_serializer_class(self):
        if self.action == 'list':
            serializer = UserSerializer
        elif self.action == 'retrieve':
            serializer = UserStatisticSerializer
        return serializer
