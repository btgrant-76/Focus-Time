# Focus-Time

This project started out as a small collection of AppleScripts and Python scripts to set up a "focus time mode" on my MacBook at work. After getting a new machine, I lost some of the permissions to keep the original setup working. This project is an attempt to get a similar setup working again.

## Background

I have been a [Pomodoro Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique) practitioner for several years now. For a while, I had been using a macOS Pomodoro timer that supported script execution at different phases of the Pomodoro "lifecycle". I had configured the timer app to quit any applications which didn't use the OS's native notification system (I'm looking at you, Microsoft Teams); at the end of the Pomodoro, the app would launch the same apps that it had quit. At the start of a Pomodoro, I'd manually disabled macOS notifications and hopefully I'd remember to re-enable the notifications at the end. 

After switching to a different Pomodoro timer, I was missing the Pomodoro start/end functionality that the original app provided. I had set up a small set of AppleScript applications and Python scripts in order to fulfill a similar set of functions, but when I switched to a new MacBook at work, I found that the AppleScripts -- a combination of keyboard shortcuts and `osascript`s for toggling Notification Center's Do Not Disturb -- no longer worked.

These days, I increasingly run a Pomodoro timer from my phone, making this project a convenient means for "decoupling" the automation of these various actions from the timer app itself.

\* That application eventually became became [Timer](https://apps.apple.com/us/app/timer-insp-by-pomodoro-tech/id799574890?mt=12).
