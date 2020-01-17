from rest_framework.pagination import PageNumberPagination


class UsersSetPagination(PageNumberPagination):
    page_size_query_param = 'users_count'
