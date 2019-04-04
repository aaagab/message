#!/usr/bin/env python3
# author: Gabriel Auger
# version: 2.0.0
# name: format_text
# license: MIT

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
try:
    from src import ft
except:
    from format_text import ft
del sys.path[0]

ft.clear_screen()
ft.clear_scrolling_history()
print(ft.success("success"))
print(ft.info("info"))
print(ft.error("error"))
print(ft.warning("warning"))

print(ft.black("color"))
print(ft.red("color"))
print(ft.green("color"))
print(ft.brown("color"))
print(ft.blue("color"))
print(ft.magenta("color"))
print(ft.cyan("color"))
print(ft.lGray("color"))
print(ft.dGray("color"))
print(ft.lRed("color"))
print(ft.lGreen("color"))
print(ft.yellow("color"))
print(ft.lBlue("color"))
print(ft.lMagenta("color"))
print(ft.lCyan("color"))
print(ft.white("color"))
print(ft.bold("emphasize"))
print(ft.uline("emphasize"))
print(ft.iverse("emphasize"))
