#!/usr/bin/env python3
import os
import sys
import time

defaults_starter = 'defaults -currentHost write ' \
                   '~/Library/Preferences/ByHost/com.apple.notificationcenterui'

dnd_cmd = f'{defaults_starter} doNotDisturb -boolean'
dnd_date_cmd = f'{defaults_starter} doNotDisturbDate -date ' \
               f'"`date -u +\"%Y-%m-%d %H:%M:%S +0000\"`"'
kill_cmd = 'killall NotificationCenter'
pomodoro_length = 25


def enable_dnd():
    os.system(dnd_cmd + ' true')
    os.system(dnd_date_cmd)
    os.system(kill_cmd)


def disable_dnd():
    os.system(dnd_cmd + ' false')
    os.system(kill_cmd)


def pause_for_focus_time(minutes):
    seconds_to_sleep = minutes * 60
    print(f'DND is enabled; sleeping for {minutes} minutes...')
    time.sleep(seconds_to_sleep)
    print('Waking up & switching off DND')


input_minutes = 0
if len(sys.argv) == 1:
    input_minutes = pomodoro_length
else:
    input_minutes = int(sys.argv[1])

enable_dnd()
pause_for_focus_time(input_minutes)
disable_dnd()
