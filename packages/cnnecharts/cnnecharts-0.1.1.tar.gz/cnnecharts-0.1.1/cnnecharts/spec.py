from typing import Dict, List, Any, Optional
import json


class Spec:
    def __init__(self, init_data: Optional[Dict] = None) -> None:
        # tree = lambda: defaultdict(tree)
        self._data = init_data or {}
        self["series"] = []

    @property
    def series(self) -> List[Any]:
        """The series property."""
        if "series" not in self._data:
            self["series"] = []

        return self["series"]

    def __getitem__(self, __key: str) -> Any:
        paths = __key.split(".")

        data = self._data
        for p in paths:

            if p not in data:
                data[p] = {}
            data = data[p]

        return data

    def __setitem__(self, key: str, value: Any):
        paths = key.split(".")

        data = self._data
        for p in paths[:-1]:
            if p not in data:
                data[p] = {}
            data = data[p]
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
