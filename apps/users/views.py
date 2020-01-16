from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import User, Statistic
from .serializers import UserListSerializer, UserDetailStatisticSerializer, DateRangeSerializer

class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def list(self, request, *args, **kwargs):
        params = request.query_params
        page_number = int(params.get('page', 1))
        users_count = int(params.get('users_count', 50))
        users = User.objects.all()[users_count * page_number - users_count:users_count * page_number]
        serializer = UserListSerializer(users, many=True)
        return Response({'data': serializer.data, 'count_users': len(User.objects.all())})


class UserStatisticApiView(APIView):
    serializer_class = UserDetailStatisticSerializer

    def get(self, request, *args, **kwargs):

        params = request.query_params
        print(params)
        serializer = DateRangeSerializer(data=params)
        if serializer.is_valid():
            print(999)
            return Response({'data': serializer.data, 'count_users': len(User.objects.all())})
        print(serializer.errors)
