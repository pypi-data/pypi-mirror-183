class Style:

    default    = {"style": 0,  "explain": "default",    "desc": "默认"}
    highlight  = {"style": 1,  "explain": "highlight",  "desc": "高亮"}
    underline  = {"style": 4,  "explain": "underline",  "desc": "下划线"}
    flash      = {"style": 5,  "explain": "flash",      "desc": "闪烁"}
    reverse    = {"style": 7,  "explain": "reverse",    "desc": "反显"}
    no_visible = {"style": 8,  "explain": "no_visible", "desc": "不可见"}

    def __init__(self, style=None):
        self._style      = style
        self._all_styles = dict()
        for name in dir(self):
            if not name.startswith("_"):
                self._all_styles[name] = getattr(self, name)

    def __get__(self, instance, owner):
        return self._set_style(self._style)

    def _set_style(self, style, _key="style"):
        # style: dict -> 查找 style[_key]
        if isinstance(style, dict) \
            and style.__contains__(_key):

            for _style in self._all_styles.values():
                if str(style[_key]) == str(_style[_key]):
                    style = _style[_key]
                    break
            else:
                style = self.default[_key]

        # style: str -> 对比各项数据
        elif isinstance(style, (str, int)):
            style = str(style).lower()
            for _style in self._all_styles.values():
                for value in _style.values():
                    if style == str(value):
                        style = _style[_key]
                        break
                else:
                    continue
                break
            else:
                style = self.default[_key]

        # style: list
        elif isinstance(style, (list, tuple)):
            style = set([self._set_style(i) for i in style])
            style = ";".join(list(style))

        # 其他
        else:
            style = self.default[_key]

        return str(style)
