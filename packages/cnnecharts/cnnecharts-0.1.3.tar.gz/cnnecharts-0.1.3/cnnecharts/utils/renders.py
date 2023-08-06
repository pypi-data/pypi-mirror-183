from jinja2 import PackageLoader, Environment
from typing import TYPE_CHECKING, Dict, Optional
from cnnecharts.utils.data_gen import json_dumps_fn
from cnnecharts.utils.baseInfos import get_root_dir

env = Environment(loader=PackageLoader("cnnecharts", "templates"))


def htmlRender(options_content: str, theme_json: Optional[str] = None):
    template = env.get_template("fileRender.html")

    if theme_json is None:
        theme_path = get_root_dir() / "templates/themes/macarons.json"
        with open(theme_path, mode="r", encoding="utf8") as f:
            theme_json = f.read()

    return template.render(options=options_content, theme=theme_json)
