from __future__ import print_function
from AppKit import NSWorkspace
import time
from foundation import *
active_window_name = ""
while True:

    new_window_name = (NSWorkspace.sharedWorkspace()
    .activeApplication()['NSApplicationName'])

    if active_window_name != new_window_name:
        active_window_name = new_window_name
        print(active_window_name)
        if active_window_name = 'Microsoft Edge Beta':
            textOfMyscript = """tell app "microsoft edge beta" to get the url of the active tab of window 1"""
            s = NSAppleScript.initWithSource_(NSAppleScript.alloc(), textOfMyscript)
            results, err = s.executeAndReturnError_(None)

            print(results.stringValue()

    time.sleep(10)