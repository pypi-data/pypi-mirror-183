import os
import platform

asked_to_bring_window_foreground = False
is_mac_os = platform.system() == "Darwin"

def bring_python_window_foreground_if_havent_before():
    """ On OSX Video stream starts in background window. This hack is needed to bring window foreground and put it over other windows"""
    global asked_to_bring_window_foreground
    global is_mac_os
    if is_mac_os == True and asked_to_bring_window_foreground == False:
        asked_to_bring_window_foreground = True
        os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
