from rest_framework.pagination import PageNumberPagination


class UsersSetPagination(PageNumberPagination):
    """
    Extends default PageNumberPagination by ``users_count`` param.
    """
    page_size_query_param = 'users_count'
