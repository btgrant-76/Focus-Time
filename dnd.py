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

# this doesn't work w/out the shortcut and w/out permissions; trying this approach instead:  https://apple.stackexchange.com/a/303400/334289
# toggle_dnd = 'osascript -e "tell application \\"System Events\\" to keystroke \\"d\\" using {command down, option down, control down}"'
# os.system(toggle_dnd)

os.system('defaults -currentHost write ~/Library/Preferences/ByHost/com.apple.notificationcenterui doNotDisturb -boolean true')
os.system('defaults -currentHost write ~/Library/Preferences/ByHost/com.apple.notificationcenterui doNotDisturbDate -date "`date -u +\"%Y-%m-%d %H:%M:%S +0000\"`"')
os.system('killall NotificationCenter')

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
# os.system(toggle_dnd)
os.system('defaults -currentHost write ~/Library/Preferences/ByHost/com.apple.notificationcenterui doNotDisturb -boolean false')
os.system('killall NotificationCenter')
