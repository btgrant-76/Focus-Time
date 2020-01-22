# Focus-Time

This project started out as a small collection of AppleScripts and Python scripts to set up a "focus time mode" on my MacBook at work. After getting a new machine, I lost some of the permissions to keep the original setup working. This project is an attempt to get a similar setup working again.

## Background

I have been a [Pomodoro Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique) practitioner for several years now. For a while, I had been using a macOS Pomodoro timer that supported script execution at different phases of the Pomodoro "lifecycle". I had configured the timer app to quit any applications which didn't use the OS's native notification system (I'm looking at you, Microsoft Teams); at the end of the Pomodoro, the app would launch the same apps that it had quit. At the start of a Pomodoro, I'd manually disabled macOS notifications and hopefully I'd remember to re-enable the notifications at the end. 

After switching to a different Pomodoro timer, I was missing the Pomodoro start/end functionality that the original app provided. I had set up a small set of AppleScript applications and Python scripts in order to fulfill a similar set of functions, but when I switched to a new MacBook at work, I found that the AppleScripts -- a combination of keyboard shortcuts and `osascript`s for toggling Notification Center's Do Not Disturb -- no longer worked.

These days, I increasingly run a Pomodoro timer from my phone, making this project a convenient means for "decoupling" the automation of these various actions from the timer app itself.

\* That application eventually became became [Timer](https://apps.apple.com/us/app/timer-insp-by-pomodoro-tech/id799574890?mt=12).

## Features

There are essentially two, different features here:  

* toggling the macOS DND (`dnd-toggle`)
* quitting/restarting the configured applications (`dnd-app`)

Some options to explore:

* Rather than *pausing/sleeping* the script the way it was being done in the first place, a coordination script to execute functions at DND start time and then either pause or schedule the next steps with `at`. The upside of the current implementation is that killing the script simply prevents future commands from running. Maybe there's a good way to do something similar with `at`.
* There could be a single command `dnd` where sub-commands could be run individually using `dnd toggle` or `dnd apps` with their respective options.
* `focus` command options
  * defaults to 25 minutes
  * manages apps found in `~/.focus-time`
  * support multiple app or time configurations
    * try out the `configparser` package
  * support a property that would specify the location of the config file
* support a applications to launch at start and quit at the end, or at least start at the beginning
* support commands like `start` and `stop` which just run the start/end operations w/out pausing in the middle

## TODOs

1. [ ] Finalize the name: "Focus Time"; the command could be `focus` instead of `dnd`
2. [ ] update the `readme` with attributions
3. [x] [try using `run` to get an application to launch in the background](https://discussions.apple.com/thread/5283675)
4. [ ] try putting up a notification at the end) indicating that DND is over 
   * [`display notification` command answer at StackExchange](https://apple.stackexchange.com/questions/57412/how-can-i-trigger-a-notification-center-notification-from-an-applescript-or-shel)
   * [AppleScript `display notification` docs](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_cmds.html#//apple_ref/doc/uid/TP40000983-CH216-SW224)
5. [x] figure out what to do w/TODOs from the original source
