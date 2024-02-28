from rest_framework.pagination import PageNumberPagination

from .constants import (
    MAX_PAGE_SIZE,
    PROJECT_PAGE_SIZE,
    PROJECT_PREVIEW_MAIN_PAGE_SIZE,
)


class ProjectPreviewMainPagination(PageNumberPagination):
    page_size = PROJECT_PREVIEW_MAIN_PAGE_SIZE
    page_size_query_param = "page_size"
    max_page_size = MAX_PAGE_SIZE


class ProjectPagination(ProjectPreviewMainPagination):
    page_size = PROJECT_PAGE_SIZE
