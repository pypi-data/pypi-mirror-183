from __future__ import annotations
from cnnecharts.optionCaller import OptionCaller
import pandas as pd
from typing import TYPE_CHECKING, Optional

from cnnecharts.spec import OptionSpec

if TYPE_CHECKING:
    from cnnecharts.mapping import Mapping


class Title(OptionCaller):
    def __init__(self, text: str) -> None:
        super().__init__()
        self.text = text

    def _ex_create_spec(self, mapping: Mapping, spec: OptionSpec):
        spec["title"] = {"text": self.text}
        return spec


class Toolbox(OptionCaller):
    """docstring for Bar."""

    def __init__(self, show=True) -> None:
        super().__init__()
        self.show = show

    def _ex_create_spec(self, mapping: Mapping, spec: OptionSpec):
        spec["toolbox"] = {"show": self.show}
        return spec


class Tooltip(OptionCaller):
    """docstring for Bar."""

    def __init__(self) -> None:
        super().__init__()

    def _ex_create_spec(self, mapping: Mapping, spec: OptionSpec):
        _ = spec["tooltip"]
        return spec
