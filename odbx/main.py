""" Lines suffixed with "# odbx" indicate that this line differs from
the reference implementation or does not exist in the reference
implementation.

"""

from lark.exceptions import VisitError
from pydantic import ValidationError
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from optimade import __api_version__
from optimade.server.routers import info, links, references, structures, landing
from optimade.server.routers.utils import BASE_URL_PREFIXES

import optimade.server.exception_handlers as exc_handlers

from . import routers  # odbx
from .routers import ABOUT

for prefix in BASE_URL_PREFIXES:
    BASE_URL_PREFIXES[prefix] = ("/optimade/" + BASE_URL_PREFIXES[prefix]).replace(
        "//", "/"
    )

app = FastAPI(
    title=ABOUT["title"],
    description=ABOUT["about"],
    version=__api_version__,
    docs_url=f"{BASE_URL_PREFIXES['major']}/extensions/docs",
    redoc_url=f"{BASE_URL_PREFIXES['major']}/extensions/redoc",
    openapi_url=f"{BASE_URL_PREFIXES['major']}/extensions/openapi.json",
)

app.add_exception_handler(StarletteHTTPException, exc_handlers.http_exception_handler)
app.add_exception_handler(
    RequestValidationError, exc_handlers.request_validation_exception_handler
)
app.add_exception_handler(ValidationError, exc_handlers.validation_exception_handler)
app.add_exception_handler(VisitError, exc_handlers.grammar_not_implemented_handler)
app.add_exception_handler(Exception, exc_handlers.general_exception_handler)

app.include_router(info.router, prefix=BASE_URL_PREFIXES["major"])
app.include_router(links.router, prefix=BASE_URL_PREFIXES["major"])
app.include_router(references.router, prefix=BASE_URL_PREFIXES["major"])
app.include_router(structures.router, prefix=BASE_URL_PREFIXES["major"])

for version in ("minor", "patch"):
    app.include_router(info.router, prefix=BASE_URL_PREFIXES[version])
    app.include_router(links.router, prefix=BASE_URL_PREFIXES[version])
    app.include_router(references.router, prefix=BASE_URL_PREFIXES[version])
    app.include_router(structures.router, prefix=BASE_URL_PREFIXES[version])
    app.include_router(landing.router, prefix=BASE_URL_PREFIXES[version])

# add landing page
app.include_router(landing.router, prefix="/optimade")
app.include_router(landing.router, prefix=BASE_URL_PREFIXES["major"])

rich_prefix = ""  # odbx
app.include_router(routers.structures.router, prefix=rich_prefix)  # odbx
app.include_router(routers.home.router, prefix=rich_prefix)  # odbx
