# Features
There are essentially two, different features here:  

* toggling the macOS DND (`dnd-toggle`)
* quitting/restarting the configured applications (`dnd-app`)

Some options to explore:

* Rather than *pausing/sleeping* the script the way it was being done in the first place, a coordination script to execute functions at DND start time and then either pause or schedule the next steps with `at`.
* There could be a single command `dnd` where sub-commands could be run individually using `dnd toggle` or `dnd apps` with their respective options.
* `focus` command options
  * defaults to 25 minutes
  * manages apps found in `~/.focus-time`
  * support multiple app or time configurations
    * probably YAML or JSON?
  * support a property that would specify the location of the config file

# TODOs
1. [ ] Finalize the name:
  * Focus Time:  the command could be `focus` instead of `dnd`
  * Something Pomodoro-related
    * focodoro
    * pomofocus
    * DnDoro
1. [ ] [try using `run` to get an application to launch in the background](https://discussions.apple.com/thread/5283675)
1. TODOs from the original source
  * [ ] try putting up a notification at the end indicating that DND is over 
  * [ ] https://apple.stackexchange.com/questions/57412/how-can-i-trigger-a-notification-center-notification-from-an-applescript-or-shel
  * [ ] https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_cmds.html#//apple_ref/doc/uid/TP40000983-CH216-SW224
