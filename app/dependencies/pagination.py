from advanced_alchemy.filters import FilterTypes, LimitOffset
from litestar.params import Parameter


def provide_limit_offset_pagination(
    current_page: int = Parameter(ge=1, query="currentPage", default=1, required=False),
    page_size: int = Parameter(
        query="pageSize",
        ge=1,
        default=10,
        required=False,
    ),
) -> FilterTypes:
    return LimitOffset(page_size, page_size * (current_page - 1))
