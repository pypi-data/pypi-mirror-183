import pandas as pd
from typing import Union, Optional, List

from cnnecharts.optionCaller import OptionCaller, OptionCallerStore


class Mapping(object):
    def __init__(
        self,
        *,
        data: Optional[pd.DataFrame] = None,
        x: Optional[str] = None,
        y: Optional[str] = None,
        color: Optional[Union[str, List[str]]] = None,
    ) -> None:
        self.data = data
        self.x = x
        self.y = y
        self.color = color

    def __add__(self, other: OptionCaller):
        if not isinstance(other, OptionCaller):
            raise TypeError("mapping 必须与 OptionCaller 相加")

        if not isinstance(other, OptionCallerStore):
            other = OptionCallerStore().add_callers(other)

        other.mapping = self
        return other

    def transform(
        self,
        data: Optional[pd.DataFrame] = None,
        x: Optional[str] = None,
        y: Optional[str] = None,
        color: Optional[Union[str, List[str]]] = None,
    ):
        data = data or self.data

        if data is None or (not isinstance(data, pd.DataFrame)):
            raise TypeError("data must be DataFrame")

        x = x or self.x
        y = y or self.y
        color = color or self.color

        if x is None:
            raise ValueError("x must be seted")

        if color is None and y is None:
            raise ValueError("y must be seted")

        def tran_data(data: pd.DataFrame, x, y, color):

            if isinstance(color, list):
                if y is not None:
                    raise ValueError("y must be none when color is list")
                return data.pivot_table(index=x, values=color, aggfunc="mean")

            return data.pivot_table(index=x, columns=color, values=y, aggfunc="mean")

        data = tran_data(data, x, y, color)

        return data, x, y, color
