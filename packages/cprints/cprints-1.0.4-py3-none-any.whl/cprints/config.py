from cprints.color import Color
from cprints.style import Style

PREFIX = "\033["
SUFFIX = "\033[0m"


class ColorPrintConfig:
    # 字体颜色
    black   = Color("black")
    red     = Color("red")
    green   = Color("green")
    yellow  = Color("yellow")
    blue    = Color("blue")
    magenta = Color("magenta")
    cyan    = Color("cyan")
    white   = Color("white")

    # 字体样式
    highlight  = Style("highlight")
    underline  = Style("underline")
    flash      = Style("flash")
    reverse    = Style("reverse")
    no_visible = Style("no_visible")

    # 默认字体颜色和样式
    default_color = Color("default")
    default_style = Style("default")

    set_style      = Style()._set_style
    set_foreground = Color()._set_foreground
    set_background = Color()._set_background
