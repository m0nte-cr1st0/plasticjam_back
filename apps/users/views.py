from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import User, Statistic
from .serializers import UserListSerializer, UserStatisticSerializer

class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    # 
    # def get_queryset(self):
    #     print(self.request.query_params)
    #     pass

class UserStatisticApiView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserStatisticSerializer
