class Color:

    default = {"fore": 39, "back": 49, "explain": "default", "desc": "默认"}
    black   = {"fore": 30, "back": 40, "explain": "black",   "desc": "黑色"}
    red     = {"fore": 31, "back": 41, "explain": "red",     "desc": "红色"}
    green   = {"fore": 32, "back": 42, "explain": "green",   "desc": "绿色"}
    yellow  = {"fore": 33, "back": 43, "explain": "yellow",  "desc": "黄色"}
    blue    = {"fore": 34, "back": 44, "explain": "blue",    "desc": "蓝色"}
    magenta = {"fore": 35, "back": 45, "explain": "magenta", "desc": "洋红"}
    cyan    = {"fore": 36, "back": 46, "explain": "cyan",    "desc": "青色"}
    white   = {"fore": 37, "back": 47, "explain": "white",   "desc": "白色"}

    def __init__(self, color=None):
        self._color      = color
        self._all_colors = dict()
        for name in dir(self):
            if not name.startswith("_"):
                self._all_colors[name] = getattr(self, name)

    def __get__(self, instance, owner):
        return dict(fore=self._set_foreground(self._color),
                    back=self._set_background(self._color))

    def _set_foreground(self, color, _key="fore"):
        # color: dict -> 查找 color[_key]
        if isinstance(color, dict) \
            and color.__contains__(_key):

            for _color in self._all_colors.values():
                if str(color[_key]) == str(_color[_key]):
                    color = _color[_key]
                    break
            else:
                color = self.default[_key]

        # color: str -> 对比各项数据
        elif isinstance(color, (str, int)):
            color = str(color).lower()
            for _color in self._all_colors.values():
                for value in _color.values():
                    if color == str(value):
                        color = _color[_key]
                        break
                else:
                    continue
                break
            else:
                color = self.default[_key]
        # 其他
        else:
            color = self.default[_key]
        return str(color)

    def _set_background(self, color, _key="back"):
        # color: dict -> 查找 color[_key]
        if isinstance(color, dict) \
            and color.__contains__(_key):

            for _color in self._all_colors.values():
                if str(color[_key]) == str(_color[_key]):
                    color = _color[_key]
                    break
            else:
                color = self.default[_key]

        # color: str -> 对比各项数据
        elif isinstance(color, (str, int)):
            color = str(color).lower()
            for _color in self._all_colors.values():
                for value in _color.values():
                    if color == str(value):
                        color = _color[_key]
                        break
                else:
                    continue
                break
            else:
                color = self.default[_key]
        # 其他
        else:
            color = self.default[_key]
        return str(color)
