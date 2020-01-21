# Детальный просмотр - фильтр
import math

from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from .models import User, Statistic
import json

class UsersTestCase(APITestCase):
    def setUp(self):
        user_data = []
        for i in range(1, 124):
            user_data.append({
                'email': 'first@mail.com'+str(i),
                'first_name': "firstname"+str(i),
                'last_name': "lastname"+str(i),
                'ip_address': "192.168.0."+str(i),
            })
        users = User.objects.bulk_create([User(**i) for i in user_data])
        self.user = User.objects.get(email='first@mail.com48')
        for i in range(1, 6):
            Statistic.objects.create(
                user=self.user,
                date='2019-10-0'+str(1+i),
                clicks=100+i,
                page_views=16+i
            )
        Statistic.objects.create(
            user=self.user,
            date='2019-10-09',
            clicks=100,
            page_views=16
        )
        self.client = APIClient()


    def test_users_list(self):
        url = reverse('users-list')
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        users_list = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['results'][47]['total_clicks'], 615)
        self.assertEqual(response.json()['results'][47]['total_page_views'], 111)
        self.assertEqual(response.json()['count'], 123)

    def test_users_pagination(self):
        url = reverse('users-list')
        self.client.force_authenticate(self.user)
        response = self.client.get(url, {'users_count': 24, 'page': 2})
        users_list = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(users_list['results']), 24)
        self.assertEqual(users_list['results'][-1]['email'], self.user.email)


    def test_user_detail(self, *args, **kwargs):
        url = reverse('users-detail', kwargs={'pk': 48})
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        user_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(user_data['user']['email'], self.user.email)
        self.assertEqual(user_data['statistics'][-2]['clicks'], 0)
        self.assertEqual(len(user_data['statistics']), 7)
        self.assertEqual(user_data['max_date'], '2019-10-09')

        url = reverse('users-detail', kwargs={'pk': 48})
        params = {'start_date': '2019-10-05', 'end_date': '2019-10-08'}
        response = self.client.get(url, params)
        user_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(user_data['statistics']), 4)
        self.assertEqual(user_data['statistics'][0]['date'], '2019-10-05')
        self.assertEqual(user_data['statistics'][3]['date'], '2019-10-08')
