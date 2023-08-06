from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Dict
import pprint
from cnnecharts.spec import OptionSpec
from cnnecharts.utils.data_gen import json_dumps_fn
import cnnecharts.utils.renders as renders

if TYPE_CHECKING:
    from cnnecharts.mapping import Mapping


class OptionCaller(object):
    def __init__(self) -> None:
        pass

    def __add__(self, other: "OptionCaller"):
        store = OptionCallerStore()

        OptionCaller._caller2store(store, self)
        OptionCaller._caller2store(store, other)

        return store

    @staticmethod
    def _caller2store(store: "OptionCallerStore", caller: "OptionCaller"):
        if isinstance(caller, OptionCallerStore):
            store.add_callers(*caller.callers)
            store.mapping = caller.mapping
        else:
            store.add_callers(caller)

    def _ex_create_spec(self, mapping: Mapping, spec: OptionSpec):
        return spec


class OptionCallerStore(OptionCaller):
    def __init__(self) -> None:
        super().__init__()
        self.mapping: Optional[Mapping] = None
        self.callers: list[OptionCaller] = []

    def add_callers(self, *caller: OptionCaller):
        self.callers.extend(caller)
        return self

    def _ex_create_spec(self, mapping: Mapping, spec: OptionSpec):
        for caller in self.callers:
            spec = caller._ex_create_spec(mapping, spec)

        return spec

    def _repr_html_(
        self,
    ):
        return pprint.pformat(self.create_option(), indent=2)

    def create_option(self, option: Optional[Dict] = None):
        if self.mapping is None:
            raise ValueError("没有设置 mapping")

        spec = OptionSpec(
            {
                "tooltip": {},
                "legend": {},
            }
            if option is None
            else option
        )

        self._ex_create_spec(self.mapping, spec)
        return spec

    def to_html(self, path: str):
        content = json_dumps_fn(self.create_option()._data)
        content = renders.htmlRender(content)

        assert isinstance(content, str)
        with open(path, mode="w", encoding="utf8") as f:
            f.write(content)
