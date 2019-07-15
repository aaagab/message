#!/usr/bin/env python3
# author: Gabriel Auger
# version: 3.1.0
# name: message
# license: MIT

import logging
import traceback
import inspect, sys, os

from ..gpkgs.format_text import ft

def error(*msgs, code=None, format="", trace=False ):
    error_msg=print_message("error", *msgs, to_print=False)
    logging.basicConfig(format=format)
    logging.error(error_msg)

    if trace is True:
        printed_trace=False
        if hasattr(traceback, 'print_stack'):
            printed_trace=True
            traceback.print_stack()

        if printed_trace is False:
            if hasattr(traceback, 'format_exc'):
                text=traceback.format_exc()
                if text is not None:
                    if text.strip() != "NoneType: None":
                        printed_trace=True
                        print(text)

        if printed_trace is False:
            print("No stack to print")

    if code is not None:
        sys.exit(code)
        
def success(*msgs, **options):
    print_message("success", *msgs)

def warning(*msgs, **options):
    print_message("warning", *msgs)

def info(*msgs, **options):
    print_message("info", *msgs)

def dbg(funct, *msgs, **options):
    if not "debug" in options:
        options["debug"]=False

    if options["debug"] is True:
        globals()[funct](*msgs, **options)

def print_message(log_type, *msgs, to_print=True):
    text=""
    if len(msgs) == 1:
        text=ft.log(log_type, "".join(msgs))
    else:
        for msg in msgs:
            text+="{}\n".format((ft.log(log_type, msg)))

    if to_print is True:
        print(text)
    else:
        return text
    