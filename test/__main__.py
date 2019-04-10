#!/usr/bin/env python3
# author: Gabriel Auger
# version: 2.0.1
# name: message
# license: MIT

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
try:
    import src as msg
except:
    import message as msg
del sys.path[0]

msg.ft.clear_scrolling_history()
print("scrolling history has been erased")

msg.ft.clear_screen()
print("screen has been cleared")

msg.title("This is a title")

msg.subtitle("This is a subtitle")
print()

msg.info("This is a single line info")
print()
msg.info(
    "This is a multiline info",
    "This is a multiline info",
    "This is a multiline info"
    )
print()
msg.warning("This is a single line warning")
print()
msg.warning(
    "This is a multiline line warning",
    "This is a multiline line warning",
    "This is a multiline line warning"
    )
print()

msg.success("This is a single line success")
print()
msg.success(
    "This is a multiline line success",
    "This is a multiline line success",
    "This is a multiline line success"
    )
print()

msg.app_error("This is a single line internal error")
print()
msg.app_error(
    "This is a multiline internal error",
    "This is a multiline internal error",
    "This is a multiline internal error",
    )
print()
msg.user_error("This is a user error")
print()
msg.user_error(
    "This is a multiline user error",
    "This is a multiline user error",
    "This is a multiline user error",
    )
print()

msg.dbg("info", "This is a debug info message", debug=True)
msg.dbg("subtitle", "This is a debug subtitle, debug can apply to any msg type", debug=True)
