from __future__ import annotations
from cnnecharts.optionCaller import OptionCaller
import pandas as pd
from typing import TYPE_CHECKING, Optional

from cnnecharts.spec import Spec, OptionSpec

if TYPE_CHECKING:
    from cnnecharts.mapping import Mapping
    from cnnecharts.seriesProps import SeriesProp

from dataclasses import dataclass, field


@dataclass
class MappingData(object):
    data: Optional[pd.DataFrame] = field(init=False, default=None)
    x: Optional[str] = field(init=False, default=None)
    y: Optional[str] = field(init=False, default=None)
    color: Optional[str] = field(init=False, default=None)


class ChartPart(OptionCaller):
    def __init__(self, *props: SeriesProp) -> None:
        super().__init__()
        self.series_callers = []
        self._mappingData = MappingData()

        for p in props:
            self.series_callers.extend(p.get_fns())

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
    def __init__(self, *props: SeriesProp) -> None:
        super().__init__(*props)

    def _ex_create_spec(self, mapping: Mapping, spec: OptionSpec):
        data = self._mappingData.data
        x = self._mappingData.x
        y = self._mappingData.y
        color = self._mappingData.color

        data, x, y, color = mapping.transform(data, x, y, color)
        data = data.round(
            2,
        )

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
                series_obj = caller(Spec(series_obj))

            spec.add_series(series_obj)

        # spec["legend.data"] = list(data.columns)

        return spec


class Line(ChartPart):
    def __init__(self, *props: SeriesProp) -> None:
        super().__init__(*props)

    def _ex_create_spec(self, mapping: Mapping, spec: OptionSpec):
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
                series_obj = caller(Spec(series_obj))

            spec.add_series(series_obj)

        spec["legend.data"] = list(data.columns)

        return spec


# class Line(ChartPart):
#     def __init__(self, *props: SeriesProp) -> None:
#         super().__init__(*props)

#     def _ex_create_spec(self, mapping: Mapping, spec: OptionSpec):
#         data = self._mappingData.data
#         x = self._mappingData.x
#         y = self._mappingData.y
#         color = self._mappingData.color

#         data, x, y, color = mapping.transform(data, x, y, color)

#         xAxis = spec["xAxis"]
#         xAxis["type"] = "category"
#         xAxis["data"] = data.index.tolist()

#         spec["yAxis.type"] = "value"

#         series = [
#             {
#                 "type": "line",
#                 "name": col,
#                 "data": list(data[col]),
#             }
#             for col in data.columns
#         ]

#         for series_obj in series:
#             for caller in self.series_callers:
#                 series_obj = caller(Spec(series_obj))

#             spec.add_series(series_obj)

#         spec["legend.data"] = list(data.columns)

#         return spec
