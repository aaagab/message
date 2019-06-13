#!/usr/bin/env python3
# author: Gabriel Auger
# version: 3.0.0
# name: message
# license: MIT

import traceback
import inspect, sys, os

from ..gpkgs.format_text import ft

def error(*msgs, trace=False):
    if len(msgs) == 1:
        print(ft.error("".join(msgs)))
    else:
        for msg in msgs:
            print(ft.error(""+msg))

    if trace is True:
        printed_trace=False
        if hasattr(traceback, 'format_exc'):
            text=traceback.format_exc()
            if text is not None:
                if text.strip() != "NoneType: None":
                    printed_trace=True
                    print(text)

        if printed_trace is False:
            if hasattr(traceback, 'print_stack'):
                traceback.print_stack()
            else:
                print("No stack to print")

def success(*msgs):
    if len(msgs) == 1:
        print(ft.success("".join(msgs)))
    else:
        for msg in msgs:
            print(ft.success(""+msg))

def warning(*msgs):
    if len(msgs) == 1:
        print(ft.warning("".join(msgs)))
    else:
        for msg in msgs:
            print(ft.warning(""+msg))

def info(*msgs):
    if len(msgs) == 1:
        print(ft.info("".join(msgs)))
    else:
        for msg in msgs:
            print(ft.info(""+msg))

def dbg(funct, *msgs, debug=False):
    if debug is True:
        globals()[funct](*msgs)
