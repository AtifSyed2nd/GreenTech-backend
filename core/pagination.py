from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    # Default number of items per page
    page_size = 200  
    # Allow the client to set the page size using 'limit' query parameter
    page_size_query_param = 'limit'
    # Maximum number of items per page
    max_page_size = 100

    # Customize the response format
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total_count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'rows': data
        })