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

application_groups = {
    'default': ['Microsoft Teams', 'Microsoft Outlook'],
    'none': [],
    'email': ['Microsoft Outlook'],
    'chat': ['Microsoft Teams']
}

pomodoro_length = 25


def tell_applications(app_list, what_to_tell):
    for app in app_list:
        script = f"osascript -e 'tell application \"{app}\"\n" \
                      f"\t{what_to_tell}\n" \
                      f"end tell\n'"
        # print(script)
        os.system(script)


def enable_dnd(apps):   # maybe start_focus instead?
    os.system(dnd_cmd + ' true')
    os.system(dnd_date_cmd)
    os.system(kill_cmd)
    tell_applications(apps, 'quit')


def disable_dnd(apps):
    os.system(dnd_cmd + ' false')
    os.system(kill_cmd)
    tell_applications(apps, 'activate')


def pause_for_focus_time(minutes):
    seconds_to_sleep = minutes * 60
    print(f'DND is enabled; sleeping for {minutes} minutes...')
    time.sleep(seconds_to_sleep)
    print('Waking up & switching off DND')


input_minutes = pomodoro_length
apps = application_groups.get('default')

if len(sys.argv) > 1:
    args = sys.argv[1:len(sys.argv)]
    for arg in args:
        print(f'arg is {arg}')
        if arg.isnumeric():
            print(f'{arg} is numeric')
            input_minutes = int(arg)
        elif application_groups.get(arg) != None:
            print(f'identified an application group:  {arg}')
            apps = application_groups.get(arg)


enable_dnd(apps)
pause_for_focus_time(input_minutes)
disable_dnd(apps)
