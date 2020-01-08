# Features

There are essentially two, different features here:  

* toggling the macOS DND (`dnd-toggle`)
* quitting/restarting the configured applications (`dnd-app`)

Some options to explore:

* Rather than *pausing/sleeping* the script the way it was being done in the first place, a coordination script to execute functions at DND start time and then either pause or schedule the next steps with `at`. The upside of the current implementation is that killing the script simply prevents future commands from running. Maybe there's a good way to do something similar with `at`.
* There could be a single command `dnd` where sub-commands could be run individually using `dnd toggle` or `dnd apps` with their respective options.
* `focus` command option  s
  * defaults to 25 minutes
  * manages apps found in `~/.focus-time`
  * support multiple app or time configurations
    * probably YAML or JSON?
  * support a property that would specify the location of the config file
* support a applications to launch at start and quit at the end, or at least start at the beginning
* support commands like `start` and `stop` which just run the start/end operations w/out pausing in the middle

## TODOs

1. [ ] Finalize the name: "Focus Time"; the command could be `focus` instead of `dnd`
2. [ ] update the `readme` with attributions
3. [ ] [try using `run` to get an application to launch in the background](https://discussions.apple.com/thread/5283675)
4. [ ] try putting up a notification at the end) indicating that DND is over 
   * [`display notification` command answer at StackExchange](https://apple.stackexchange.com/questions/57412/how-can-i-trigger-a-notification-center-notification-from-an-applescript-or-shel)
   * [AppleScript `display notification` docs](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_cmds.html#//apple_ref/doc/uid/TP40000983-CH216-SW224)
5. [x] figure out what to do w/TODOs from the original source
