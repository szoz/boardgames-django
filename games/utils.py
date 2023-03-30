from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class SimplePagePagination(PageNumberPagination):
    """Pagination by page and number but with simple response - only results and no pagination metadate."""

    page_size_query_param = "limit"

    def get_paginated_response(self, data: list | dict) -> Response:
        return Response(data, headers={"X-Total-Count": self.page.paginator.count})
