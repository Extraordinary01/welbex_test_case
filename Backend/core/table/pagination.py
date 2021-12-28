from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class TablePagination(PageNumberPagination):
    page_size = 3

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'page' : self.page.number,
            'amount_pages': self.page.paginator.num_pages,
            'results': data
        })