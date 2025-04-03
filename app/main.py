from litestar import Litestar, Router
from litestar.di import Provide

from app.controllers.user import UserController
from app.db import alchemy
from app.dependencies.pagination import provide_limit_offset_pagination

router = Router(
    path="/api/v1",
    route_handlers=(UserController,),
)


app = Litestar(
    route_handlers=(router,),
    plugins=(alchemy,),
    dependencies={
        "limit_offset": Provide(provide_limit_offset_pagination, sync_to_thread=False),
    },
)
