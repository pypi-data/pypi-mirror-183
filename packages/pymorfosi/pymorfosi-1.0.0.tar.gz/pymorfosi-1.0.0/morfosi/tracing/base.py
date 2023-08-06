import traceback
from typing import Any, Optional, Union
import wrapt

from morfosi.registry import DEFAULT_REGISTRY, Registry
from morfosi.schema import TracerOptions, Path


class BaseTracer(wrapt.ObjectProxy):
    def __init__(
        self,
        wrapped: Any,
        registry: Optional[Registry] = None,
        path: Path = [],
        options: TracerOptions = TracerOptions(),
    ):
        super().__init__(wrapped)

        self._self_tracer_registry = registry if registry else DEFAULT_REGISTRY
        self._self_tracer_path = path
        self._self_tracer_options = options

    def resolve_path(self, name: Union[str, int]) -> Path:
        if len(self._self_tracer_path) > 0:
            return self._self_tracer_path + [name]
        else:
            return [name]

    def resolve_stack(self) -> str:
        return traceback.format_stack()
