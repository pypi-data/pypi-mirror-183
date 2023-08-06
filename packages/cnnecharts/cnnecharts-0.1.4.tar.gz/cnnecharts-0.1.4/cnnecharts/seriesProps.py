from __future__ import annotations
from cnnecharts.optionCaller import OptionCaller
import pandas as pd
from typing import TYPE_CHECKING, Optional, Callable, List
from functools import wraps

if TYPE_CHECKING:
    from cnnecharts.spec import Spec


class SeriesProp(object):
    def __init__(self) -> None:
        self.__fns: List[Callable] = []

    def _add_fns(self, *fns: Callable):
        self.__fns.extend(fns)
        return self

    def __add__(self, other: "SeriesProp"):
        newProp = SeriesProp()
        newProp._add_fns(*self.__fns, *other.__fns)

        return newProp

    def get_fns(self):
        return self.__fns


def _defineProp(fn):
    return SeriesProp()._add_fns(fn)


def id(id: str):
    def fn(series_obj: Spec):
        if series_obj.has("name"):
            series_obj["id"] = f'{series_obj["name"]}_{id}'
        else:
            series_obj["id"] = id
        return series_obj

    return _defineProp(fn)


class onUniversalTransition(SeriesProp):
    """开启动画效果"""

    def __init__(self, duration: int) -> None:

        super().__init__()

        def fn(series_obj):
            series_obj["universalTransition"] = True
            series_obj["animationDurationUpdate"] = duration
            return series_obj

        self._add_fns(fn)


class background(SeriesProp):
    def __init__(self, color: str) -> None:
        super().__init__()

        def fn(series_obj):
            series_obj["showBackground"] = True
            series_obj["backgroundStyle.color"] = color
            return series_obj

        self._add_fns(fn)


class emphasis(SeriesProp):
    def __init__(self, focus: str = "self") -> None:
        super().__init__()

        def fn(series_obj):
            series_obj["emphasis.focus"] = focus
            series_obj["emphasis.label.show"] = True
            return series_obj

        self._add_fns(fn)


class stack(SeriesProp):
    def __init__(self, stack: str = "total") -> None:
        super().__init__()

        def fn(series_obj):
            series_obj["stack"] = stack
            return series_obj

        self._add_fns(fn)


class label(SeriesProp):
    def __init__(self, formatter=r"{c}") -> None:
        """
        标签内容格式器，支持字符串模板和回调函数两种形式，字符串模板与回调函数返回的字符串均支持用 \n 换行。

        字符串模板 模板变量有：

        {a}：系列名。
        {b}：数据名。
        {c}：数据值。
        {@xxx}：数据中名为 'xxx' 的维度的值，如 {@product} 表示名为 'product' 的维度的值。
        {@[n]}：数据中维度 n 的值，如 {@[3]} 表示维度 3 的值，从 0 开始计数。
        示例：

        formatter: '{b}: {@score}'
        """
        super().__init__()

        def fn(series_obj):
            series_obj["label.show"] = True
            series_obj["label.formatter"] = formatter
            return series_obj

        self._add_fns(fn)
