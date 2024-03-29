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
    'default': ['Microsoft Teams', 'Microsoft Outlook', 'Messages'],
    'none': [],
    'email': ['Microsoft Outlook'],
    'chat': ['Microsoft Teams', 'Messages']
}

notification_start = "osascript -e 'display notification \""
notification_end = "\" with title \"Focus Time is Over\"'"

startup_message = "Remember to disable notifications on other devices!"
end_message = "Remember to enable notifications on other devices!"

pomodoro_length = 25


def tell_applications(app_list, what_to_tell):
    for app in app_list:
        script = f"osascript -e 'tell application \"{app}\"\n" \
                      f"\t{what_to_tell}\n" \
                      f"end tell\n'"
        # print(script)
        os.system(script)


def enable_dnd(apps):   # maybe start_focus instead?
    if startup_message is not None:
        os.system(f"{notification_start}{startup_message}\"with title \"Focus Time is Beginning\"'")
        print(f'{startup_message} Press enter to continue...')
        input()

    os.system(dnd_cmd + ' true')
    os.system(dnd_date_cmd)
    os.system(kill_cmd)
    tell_applications(apps, 'quit')


def disable_dnd(apps):
    os.system(dnd_cmd + ' false')
    os.system(kill_cmd)

    # run will get "well-behaved" applications to launch silently
    # https://discussions.apple.com/thread/5283675
    tell_applications(apps, 'run')


def pause_for_focus_time(minutes):
    seconds_to_sleep = minutes * 60
    print(f'DND is enabled; sleeping for {minutes} minutes...')
    time.sleep(seconds_to_sleep)
    print('Waking up & switching off DND')

    if end_message is not None:
        os.system(f"{notification_start}{end_message}{notification_end}")
        print(end_message)
    else:
        os.system(f"{notification_start}{notification_end}")


input_minutes = pomodoro_length
apps = application_groups.get('default')

if len(sys.argv) > 1:
    args = sys.argv[1:len(sys.argv)]
    for arg in args:
        # print(f'arg is {arg}')
        if arg.isnumeric():
            # print(f'{arg} is numeric')
            input_minutes = int(arg)
        elif application_groups.get(arg):
            # print(f'identified an application group:  {arg}')
            apps = application_groups.get(arg)


enable_dnd(apps)
pause_for_focus_time(input_minutes)
disable_dnd(apps)
