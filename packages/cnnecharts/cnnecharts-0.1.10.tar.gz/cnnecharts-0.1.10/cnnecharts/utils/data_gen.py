import base64
from datetime import datetime
from enum import Enum
from pathlib import Path
from json import JSONEncoder, dumps
from functools import partial
import numpy as np
import pandas as pd


def _nan2None(obj):
    if isinstance(obj, dict):
        return {k: _nan2None(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_nan2None(v) for v in obj]
    elif isinstance(obj, float) and pd.isna(obj):
        return None
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, datetime):
        return str(obj)

    return obj


class _NanConverter(JSONEncoder):
    def default(self, obj):
        # possible other customizations here
        pass

    def encode(self, obj, *args, **kwargs):
        obj = _nan2None(obj)
        return super().encode(obj, *args, **kwargs)

    def iterencode(self, obj, *args, **kwargs):
        obj = _nan2None(obj)
        return super().iterencode(obj, *args, **kwargs)


json_dumps_fn = partial(dumps, cls=_NanConverter)
