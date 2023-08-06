# print color text to terminal

from cprints import cp


cp.cprint("Hello World", fg=cp.red, bg=cp.black, style=cp.underline)
cp.print_red("Hello World", style=cp.highlight)