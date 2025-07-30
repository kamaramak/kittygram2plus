from rest_framework.pagination import BasePagination


class CatsPagination(BasePagination):
    page_size = 20