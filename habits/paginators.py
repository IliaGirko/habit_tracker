from rest_framework.pagination import PageNumberPagination


class HabitsPaginator(PageNumberPagination):
    """ Пагинатор ограничивающий выборку до пяти элементов на странице """
    page_size = 5
