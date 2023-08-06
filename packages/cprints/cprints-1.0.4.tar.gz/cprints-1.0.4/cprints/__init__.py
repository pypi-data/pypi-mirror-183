from cprints.color import Color as colors
from cprints.style import Style as styles
from cprints.main  import ColorPrint


cp = ColorPrint()

# 彩色打印
cprint        = cp.cprint
print_black   = cp.print_black
print_red     = cp.print_red
print_green   = cp.print_green
print_yellow  = cp.print_yellow
print_blue    = cp.print_blue
print_magenta = cp.print_magenta
print_cyan    = cp.print_cyan
print_white   = cp.print_white

# 着色文本
colored         = cp.colored
colored_black   = cp.colored_black
colored_red     = cp.colored_red
colored_green   = cp.colored_green
colored_yellow  = cp.colored_yellow
colored_blue    = cp.colored_blue
colored_magenta = cp.colored_magenta
colored_cyan    = cp.colored_cyan
colored_white   = cp.colored_white

# 进度条
progress_bar    = cp.progress_bar

__all__ = ["cp", "colors", "styles"]
