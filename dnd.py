#!/usr/bin/env python3
import os
import sys
import time

# TODOs
# Create a README
# First you've got to set up a keyboard shortcut for enabling/disabling Do Not Disturb. I could link to the *Overflow article about it.
# try putting up a notification at the end indicating that DND is over 
# * https://apple.stackexchange.com/questions/57412/how-can-i-trigger-a-notification-center-notification-from-an-applescript-or-shel
# * https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_cmds.html#//apple_ref/doc/uid/TP40000983-CH216-SW224
# 

toggle_dnd = 'osascript -e "tell application \\"System Events\\" to keystroke \\"d\\" using {command down, option down, control down}"'
os.system(toggle_dnd)

pomodoro_length = 25 

minutes = 0

if len(sys.argv) == 1:  
    minutes = pomodoro_length
else: 
    minutes = int(sys.argv[1])

minutes_to_sleep = minutes * 60

print(f'DND is enabled; sleeping for {minutes} minutes...')
time.sleep(minutes_to_sleep)

print('Waking up & switching off DND')
os.system(toggle_dnd)
