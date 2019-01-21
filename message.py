#!/usr/bin/env python3
# author: Gabriel Auger
# version: 0.1.0
# name: message
# license: MIT

import traceback
import inspect, sys, os, json

from format_text import Format_text as ft

def app_error(*msgs):
    if len(msgs) == 1:
        print(ft.error("".join(msgs)))
    else:
        for msg in msgs:
            print(ft.error(""+msg))
    # frame,filename,line_number,function_name,lines,index=inspect.stack()[1]
    # print("\t"+str(line_number)+": "+filename)
    traceback.print_stack()
    traceback.format_exc()

def user_error(*msgs):
    if len(msgs) == 1:
        print(ft.error("".join(msgs)))
    else:
        for msg in msgs:
            print(ft.error(""+msg))

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


def raw_print(msg):
    print(msg)

def draw_line(char, n):
    tmp_str=""
    for i in range(0, n):
        tmp_str+=char

    return tmp_str

def title(msg):
    print()
    print(ft.lGreen("  @@@@ ")+ft.bold(msg)+ft.lGreen(" @@@@"))
    print()

def subtitle(msg):
    print()
    ldeco="### "
    rdeco=""
    tmp_str=ldeco+msg+rdeco;
    print("  "+ft.lBlue(ldeco)+ft.bold(msg)+ft.lCyan(rdeco))

def dbg(funct, *msgs):
    filen_main=os.path.basename(sys.argv[0])
    unique_paths=[]
    data={}
    debug=False
    for direpa in sys.path:
        if direpa not in unique_paths:
            filenpa_main=os.path.join(direpa, filen_main)
            if os.path.exists(filenpa_main):
                filenpa_config=os.path.join(direpa, "config", "config.json")
                if os.path.exists(filenpa_config):
                    with open(filenpa_config, "r") as f:
                        try:
                            data=json.load(f)
                        except:
                            pass

                    if "debug" in data and data["debug"] is True:
                        debug=True
                        break         

        if not unique_paths:
            unique_paths.append(direpa)

    if debug is True:
        globals()[funct](*msgs)
        return True
    else:
        return False
