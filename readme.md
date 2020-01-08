# Focus-Time

This project started out as a small collection of AppleScripts and Python scripts to set up a "focus time mode" on my work MacBook. After getting a new machine &amp; I lost some of the permissions to keep the original setup work, I decided to try a different setup.

## Background

I have been a practitioner of the [Pomodoro Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique) for several years now, in varying degrees. I had been using a macOS Pomodoro timer application for a while (which became [Timer](https://apps.apple.com/us/app/timer-insp-by-pomodoro-tech/id799574890?mt=12)) that supported scripts being run at different phases of the Pomodoro "lifecycle". At the time, I would manually disabled macOS notifications at the start of my Pomodoro and then configure the app quit other applications which didn't use the OS's native notification system (I'm looking at you, Microsoft Teams). At the end of the Pomodoro, the app would launch the apps that it had quit at the start and hopefully I would remember to re-enable the macOS notifications.

After switching to a different Pomodoro timer, I was missing the Pomodoro start/end functionality that Timer provided. I had set up a small set of AppleScript applications and Python scripts in order to fulfill a similar set of functions, but when I switched to a new MacBook at work, I found that the AppleScripts -- a combination of keyboard shortcuts and `osascript`s for toggling Notification Center's Do Not Disturb -- no longer worked.