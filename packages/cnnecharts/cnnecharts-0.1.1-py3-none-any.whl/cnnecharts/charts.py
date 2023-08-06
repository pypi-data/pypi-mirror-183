from __future__ import annotations
from cnnecharts.optionCaller import OptionCaller
import pandas as pd
from typing import TYPE_CHECKING, Optional

from cnnecharts.spec import Spec

if TYPE_CHECKING:
    from cnnecharts.mapping import Mapping

from dataclasses import dataclass, field


@dataclass
class MappingData(object):
    data: Optional[pd.DataFrame] = field(init=False, default=None)
    x: Optional[str] = field(init=False, default=None)
    y: Optional[str] = field(init=False, default=None)
    color: Optional[str] = field(init=False, default=None)


class ChartPart(OptionCaller):
    def __init__(self, *, id: Optional[str] = None) -> None:
        super().__init__()
        self.series_callers = []
        self._mappingData = MappingData()

        if id:

            def set_fn(series_obj):
                if "name" in series_obj:
                    series_obj["id"] = f'{series_obj["name"]}_{id}'
                else:
                    series_obj["id"] = id
                return series_obj

            self.series_callers.append(set_fn)

    def mapping(
        self,
        *,
        data: Optional[pd.DataFrame] = None,
        x: Optional[str],
        y: Optional[str],
        color: Optional[str],
    ):
        self._mappingData.data = data
        self._mappingData.x = x
        self._mappingData.y = y
        self._mappingData.color = color

        return self


class Bar(ChartPart):
    def __init__(self, *, id: Optional[str] = None) -> None:
        super().__init__(id=id)

    def onUniversalTransition(self):
        """开启动画效果"""

        def set_fn(series_obj):
            series_obj["universalTransition"] = True
            series_obj["animationDurationUpdate"] = 1000
            return series_obj

        self.series_callers.append(set_fn)
        return self

    def background(self, color: str):
        def set_fn(series_obj):
            series_obj["showBackground"] = True
            series_obj["backgroundStyle.color"] = color
            return series_obj

        self.series_callers.append(set_fn)

        return self

    def emphasis(self, focus="self"):
        def set_fn(series_obj):
            series_obj["emphasis.focus"] = focus
            return series_obj

        self.series_callers.append(set_fn)

        return self

    def _ex_create_spec(self, mapping: Mapping, spec: Spec):
        data = self._mappingData.data
        x = self._mappingData.x
        y = self._mappingData.y
        color = self._mappingData.color

        data, x, y, color = mapping.transform(data, x, y, color)

        xAxis = spec["xAxis"]
        xAxis["type"] = "category"
        xAxis["data"] = data.index.tolist()

        spec["yAxis.type"] = "value"

        series = [
            {
                "type": "bar",
                "name": col,
                "data": list(data[col]),
            }
            for col in data.columns
        ]

        for series_obj in series:
            for caller in self.series_callers:
                series_obj = caller(series_obj)

            spec.series.append(series_obj)

        spec["legend.data"] = list(data.columns)

        return spec


class Line(ChartPart):
    def __init__(self, *, id: Optional[str] = None) -> None:
        super().__init__(id=id)

    def onUniversalTransition(self):
        """开启动画效果"""

        def set_fn(series_obj):
            series_obj["universalTransition"] = True
            series_obj["animationDurationUpdate"] = 1000
            return series_obj

        self.series_callers.append(set_fn)
        return self

    def background(self, color: str):
        def set_fn(series_obj):
            series_obj["showBackground"] = True
            series_obj["backgroundStyle.color"] = color
            return series_obj

        self.series_callers.append(set_fn)

        return self

    def emphasis(self, focus="self"):
        def set_fn(series_obj):
            series_obj["emphasis.focus"] = focus
            return series_obj

        self.series_callers.append(set_fn)

        return self

    def _ex_create_spec(self, mapping: Mapping, spec: Spec):
        data = self._mappingData.data
        x = self._mappingData.x
        y = self._mappingData.y
        color = self._mappingData.color

        data, x, y, color = mapping.transform(data, x, y, color)

        xAxis = spec["xAxis"]
        xAxis["type"] = "category"
        xAxis["data"] = data.index.tolist()

        spec["yAxis.type"] = "value"

        series = [
            {
                "type": "line",
                "name": col,
                "data": list(data[col]),
            }
            for col in data.columns
        ]

        for series_obj in series:
            for caller in self.series_callers:
                series_obj = caller(series_obj)

            spec.series.append(series_obj)

        spec["legend.data"] = list(data.columns)

        return spec
