#!/usr/bin/env python3
# author: Gabriel Auger
# version: 6.1.0
# name: message
# license: MIT

if __name__ == "__main__":
    import sys, os
    import importlib
    direpa_script_parent=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    module_name=os.path.basename(os.path.dirname(os.path.realpath(__file__)))
    sys.path.insert(0, direpa_script_parent)
    msg = importlib.import_module(module_name)
    del sys.path[0]

    msg.ft.clear_scrolling_history()
    print("scrolling history has been erased")

    msg.ft.clear_screen()
    print("screen has been cleared")

    msg.info("This is a single line info")
    print()
    msg.info(
        "This is a multiline info",
        "This is a multiline info",
        "This is a multiline info"
        )
    print()

    mylist=[ 
        "line one '{}'", 
        "line two '{}'", 
        "line tree '{}'" ]
    msg.info("An array is given \"{}\" instead of multiple lines".format(mylist))
    print()
    msg.info(mylist)
    print()

    keys=["first_value", "second_value", "third_value"]
    msg.info("keys list \"{}\" is given to populate empty fields '{{}}'".format(keys,))
    print()
    msg.info(mylist, keys=keys)
    print()

    mylist=[ 
        "line one '{first}'", 
        "line two '{second}'", 
        "line tree '{first} and '{third}''" 
    ]
    keys={
        "first":"first_value", 
        "second":"second_value", 
        "third":"third_value"
    }
    msg.info("It also work with keywords")
    print()
    msg.info(mylist, keys=keys)
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

    msg.error("This is a single line error")
    print()
    msg.error(
        "This is a multiline error",
        "This is a multiline error",
        "This is a multiline error",
        )
    print()
    msg.error("This is a single error with traceback", trace=True)
    print()
    msg.error(
        "This is a multiline user error with traceback",
        "This is a multiline user error with traceback",
        "This is a multiline user error with traceback",
        trace=True
        )
    print()

    msg.info("Debug message printed", debug=True)
    msg.info("Debug message not printed", debug=False)

    print()
    text="You can create custom messages too"
    print(msg.ft.lGreen("  @@@@ ")+msg.ft.bold(text)+msg.ft.lGreen(" @@@@"))
    print()
    ldeco="### "
    rdeco=""
    tmp_str=ldeco+text+rdeco;
    print("  "+msg.ft.lBlue(ldeco)+msg.ft.bold(text)+msg.ft.lCyan(rdeco))
    print()

    msg.error("This is an error with stack trace and system exit with code 1", exit=1, trace=True)
