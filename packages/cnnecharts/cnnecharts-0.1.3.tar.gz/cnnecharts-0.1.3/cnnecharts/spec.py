from typing import Dict, List, Any, Optional
import json


class Spec:
    def __init__(self, init_data: Optional[Dict] = None) -> None:
        data = {} if init_data is None else init_data
        if isinstance(init_data, Spec):
            data = init_data._data

        self._data = data

    def has(self, key: str):
        return key in self._data

    def __getitem__(self, key: str) -> "Spec":
        paths = key.split(".")

        data = self._data
        for p in paths:

            if p not in data:
                data[p] = {}
            data = data[p]

        if isinstance(data, dict):
            return Spec(data)
        return data

    def __setitem__(self, key: str, value: Any):
        paths = key.split(".")

        data = self._data
        for p in paths[:-1]:
            if p not in data:
                data[p] = {}
            data = data[p]

        if isinstance(value, Spec):
            value = value._data

        data[paths[-1]] = value

    def __delitem__(self, key: str):
        paths = key.split(".")

        data = self._data
        for p in paths[:-1]:
            if p not in data:
                data[p] = {}
            data = data[p]

        del data[paths[-1]]

    def __str__(self) -> str:
        return json.dumps(self._data, indent=2)

    def __repr__(self) -> str:
        return str(self)


class OptionSpec(Spec):
    def __init__(self, init_data: Optional[Dict] = None) -> None:
        super().__init__(init_data)
        self["series"] = []

    def add_series(self, obj: Dict):
        if isinstance(obj, Spec):
            obj = obj._data
        self._data["series"].append(obj)

    # @property
    # def series(self) -> List[Any]:
    #     """The series property."""
    #     if "series" not in self._data:
    #         self["series"] = []

    #     return self["series"]
