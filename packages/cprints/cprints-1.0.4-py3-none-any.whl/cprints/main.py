import math
from cprints.config import (
    PREFIX, SUFFIX, ColorPrintConfig)


class BasePrint(ColorPrintConfig):

    def colored(self, text, /, *args, fg=None, bg=None, style=None, suffix=True):
        """\
        :params text   : 着色文本
        :params *args  : 着色可变参数
        :params fg     : 前景色(black, red, green, yellow, blue, magenta, cyan, white)
        :params bg     : 背景色(black, red, green, yellow, blue, magenta, cyan, white)
        :params style  : 文本样式(default, highlight, underline, flash, reverse)
        :params suffix : 恢复默认打印方式

        explain:
            from cprints import cp
            text = cp.colored("Hello World", fg=cp.red, bg=cp.black, style=cp.underline)
            print(text)
        """
        fg     = self.set_foreground(fg)
        bg     = self.set_background(bg)
        style  = self.set_style(style)
        suffix = SUFFIX if bool(suffix) else ""
        args = " ".join([str(i) for i in args])
        if args:
            args = " " + args
        return f"{PREFIX}{style};{fg};{bg}m{text}{args}{suffix}"

    def cprint(self, text, /, *args, fg=None, bg=None, style=None, suffix=True, **kwargs):
        """\
        :params text     : 着色文本
        :params *args    : 着色可变参数
        :params fg       : 前景色(black, red, green, yellow, blue, magenta, cyan, white)
        :params bg       : 背景色(black, red, green, yellow, blue, magenta, cyan, white)
        :params style    : 文本样式(default, highlight, underline, flash, reverse)
        :params suffix   : 恢复默认打印方式
        :params **kwargs : print的关键字参数

        explain:
            from cprints import cp
            cp.cprint("Hello World", fg=cp.red, bg=cp.black, style=cp.underline)
        """
        fg     = self.set_foreground(fg)
        bg     = self.set_background(bg)
        style  = self.set_style(style)
        suffix = SUFFIX if bool(suffix) else ""
        args = " ".join([str(i) for i in args])
        if args:
            args = " " + args
        print(f"{PREFIX}{style};{fg};{bg}m{text}{args}{suffix}", **kwargs)

    def progress_bar(self, now: int, total: int, lenght=36, desc="", bar=b"\xe2\x94\x81", pad=""):
        """\
        :params now    : 当前进度值
        :params total  : 总进度值
        :params lenght : 进度条长度
        :params desc   : 进度条介绍
        :params bar    : 进度条 进度填充
        :params pad    : 进度条 其余填充

        explain:
            from cprints import cp
            maximum = 100
            for i in range(1, maximum+1):
                cp.progress_bar(now=i, total=maximum)
        """
        now = total if now >= total else now
        bar = bar.decode() if isinstance(bar, bytes) else str(bar)
        # 百分比
        percent = now / total
        # 进度条总长度
        total_bar = len(self.colored(lenght * bar))
        foreground = self.red if now < total else self.green
        # 进度条
        progress_bar = self.colored(
            math.floor(percent * lenght) * bar, fg=foreground)
        # 需要打印的百分比
        percent = self.colored(f"{percent:.2%}", style=self.underline)
        end = "\n" if now >= total else ""
        print(f"\r<{desc}{progress_bar:{pad}<{total_bar}}> {percent} [{now}/{total}]", end=end, flush=True)


class Colored(BasePrint):

    def colored_black(self, text, /, *args, bg=None, style=None, suffix=True):
        return self.colored(text, *args, fg=self.black, bg=bg, style=style, suffix=suffix)

    def colored_red(self, text, /, *args, bg=None, style=None, suffix=True):
        return self.colored(text, *args, fg=self.red, bg=bg, style=style, suffix=suffix)

    def colored_green(self, text, /, *args, bg=None, style=None, suffix=True):
        return self.colored(text, *args, fg=self.green, bg=bg, style=style, suffix=suffix)

    def colored_yellow(self, text, /, *args, bg=None, style=None, suffix=True):
        return self.colored(text, *args, fg=self.yellow, bg=bg, style=style, suffix=suffix)

    def colored_blue(self, text, /, *args, bg=None, style=None, suffix=True):
        return self.colored(text, *args, fg=self.blue, bg=bg, style=style, suffix=suffix)

    def colored_magenta(self, text, /, *args, bg=None, style=None, suffix=True):
        return self.colored(text, *args, fg=self.magenta, bg=bg, style=style, suffix=suffix)

    def colored_cyan(self, text, /, *args, bg=None, style=None, suffix=True):
        return self.colored(text, *args, fg=self.cyan, bg=bg, style=style, suffix=suffix)

    def colored_white(self, text, /, *args, bg=None, style=None, suffix=True):
        return self.colored(text, *args, fg=self.white, bg=bg, style=style, suffix=suffix)


class ColorPrint(Colored):

    def print_black(self, text ,/, *args, bg=None, style=None, suffix=True, **kwargs):
        self.cprint(text, *args, fg=self.black, bg=bg, style=style, suffix=suffix, **kwargs)

    def print_red(self, text, /, *args, bg=None, style=None, suffix=True, **kwargs):
        self.cprint(text, *args, fg=self.red, bg=bg, style=style, suffix=suffix, **kwargs)

    def print_green(self, text, /, *args, bg=None, style=None, suffix=True, **kwargs):
        self.cprint(text, *args, fg=self.green, bg=bg, style=style, suffix=suffix, **kwargs)

    def print_yellow(self, text, /, *args, bg=None, style=None, suffix=True, **kwargs):
        self.cprint(text, *args, fg=self.yellow, bg=bg, style=style, suffix=suffix, **kwargs)

    def print_blue(self, text, /, *args, bg=None, style=None, suffix=True, **kwargs):
        self.cprint(text, *args, fg=self.blue, bg=bg, style=style, suffix=suffix, **kwargs)

    def print_magenta(self, text, /, *args, bg=None, style=None, suffix=True, **kwargs):
        self.cprint(text, *args, fg=self.magenta, bg=bg, style=style, suffix=suffix, **kwargs)

    def print_cyan(self, text, /, *args, bg=None, style=None, suffix=True, **kwargs):
        self.cprint(text, *args, fg=self.cyan, bg=bg, style=style, suffix=suffix, **kwargs)

    def print_white(self, text, /, *args, bg=None, style=None, suffix=True, **kwargs):
        self.cprint(text, *args, fg=self.white, bg=bg, style=style, suffix=suffix, **kwargs)
