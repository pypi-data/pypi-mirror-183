import re
from collections.abc import Callable
from typing import Any

from beartype import beartype
from fastapi import APIRouter as _APIRouter
from fastapi.types import DecoratedCallable


_PATTERN = re.compile(r"(^/$)|(^.+[^\/]$)")


class APIRouter(_APIRouter):
    """Subclass of `APIRouter` which handles paths with & without trailing
    slashes.
    """

    @beartype
    def api_route(
        self, *, path: str, include_in_schema: bool = True, **kwargs: Any
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        if _PATTERN.search(path):
            return super().api_route(
                path, include_in_schema=include_in_schema, **kwargs
            )
        else:
            raise ValueError(f"Invalid route: {path}")
