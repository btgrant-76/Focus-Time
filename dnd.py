#!/usr/bin/env python3
import os
import sys
import time

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

os.system('defaults -currentHost write ~/Library/Preferences/ByHost/com.apple.notificationcenterui doNotDisturb -boolean false')
os.system('killall NotificationCenter')
