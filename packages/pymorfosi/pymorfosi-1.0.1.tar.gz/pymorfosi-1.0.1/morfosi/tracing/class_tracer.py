from typing import Any, Optional

from morfosi.schema import Change, Add, Delete, Path, TracerOptions
from morfosi.registry import Registry
from morfosi.tracing.base import BaseTracer
from morfosi.tracing.utils import is_primitive, is_morfosi_builtin
from morfosi.tracing.snapshot import snapshot


class ClassTracer(BaseTracer):
    def __init__(
        self,
        wrapped: Any,
        registry: Optional[Registry] = None,
        path: Path = [],
        options: TracerOptions = TracerOptions(),
    ):
        super().__init__(wrapped, registry=registry, path=path, options=options)

        from morfosi.tracing.trace import traceable

        for field, value in wrapped.__dict__.items():
            if not is_primitive(value) and not is_morfosi_builtin(field):
                wrapped.__dict__[field] = traceable(
                    value, registry=registry, path=path + [field], options=options
                )
                pass

    def __setattr__(self, name: str, value: Any):
        if is_morfosi_builtin(name):
            return super().__setattr__(name, value)  # type: ignore

        path = self.resolve_path(name)
        stack = self.resolve_stack()
        wrapped: object = self.__wrapped__  # type: ignore

        value_snapshot = snapshot(
            value, self._self_tracer_options.value_snapshot_strategy
        )

        if name in wrapped.__dict__:
            action = Change(
                path=path,
                old_value=snapshot(
                    wrapped.__dict__[name],
                    self._self_tracer_options.value_snapshot_strategy,
                ),
                new_value=value_snapshot,
                stack=stack,
            )
        else:
            action = Add(path=path, new_value=value_snapshot, stack=stack)

        self._self_tracer_registry.append(action)

        if not is_primitive(value):
            from morfosi.tracing.trace import traceable

            value = traceable(
                value,
                registry=self._self_tracer_registry,
                path=path,
                options=self._self_tracer_options,
            )

        return super().__setattr__(name, value)  # type: ignore

    def __delattr__(self, name: str):
        path = self.resolve_path(name)
        stack = self.resolve_stack()

        wrapped: object = self.__wrapped__  # type: ignore
        old_value = wrapped.__dict__.get(name)

        self._self_tracer_registry.append(
            Delete(
                path=path,
                old_value=snapshot(
                    old_value, self._self_tracer_options.value_snapshot_strategy
                ),
                stack=stack,
            )
        )

        return super().__delattr__(name)  # type: ignore
