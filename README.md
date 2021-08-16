# jira-cli-via-go-jira README

:sweat_drops: a JIRA CLI (command line interface) to dump a summary of the state of the current sprint. Uses the go-jira library.

## Reference

https://github.com/go-jira/jira

---

## Dependencies

### Python 3

You need to install `Python 3` on your machine.

Use the `Windows Installer (64 bit)` from the official Python site:

https://www.python.org/downloads/windows/

### Git bash

`sh` is required for the python script.

Download from https://gitforwindows.org/

### System PATH environment variable

The scripts in this project assume that the locations of `python` and `sh` are included in the `PATH` environment variable.

---

## Usage

### Login

1. create the API token via the Jira website

   - click on your avatar
   - select Account settings
   - select Security
   - Under API Token, select Create and manage API tokens
   - select Create API Token
   - give the token an appropriate name
   - copy the token value

2. configure Go-Jira (see ref section above) for endpoint, user, project - this is the `.jira-d/config.yml` file

    note: you need to remove the curly brackets.

3. create a script to set JIRA_API_TOKEN

    This script will store the token value you received in step 1

    Create a text file named `set-jira-api-token-env-var.bat`

    The content needs to be as follows, but with the value of the token inserted:

    ```
    @ECHO OFF
    SET JIRA_API_TOKEN={token value}
    ```

    note: you need to remove the curly brackets.

4. run the script `set-jira-api-token-env-var.bat`

5. login

    Open a `cmd` command line prompt (NOT PowerShell) at this README location.

    `jira session`

### Read data from JIRA

6. run the test script (it is only reading, not writing!)

    This is to check everything is setup OK.

    This script dumps a text report of the current sprint status, with stories + bugs ranked and grouped by status.

    `test_dump_current_sprint_state_sos.bat`

7. see the available options

    `go.bat`

    ```
    usage: parse_current_sprint_issues.py [-h] -j JSON -s SPRINT_NAME -g GOAL [-o]
    parse_current_sprint_issues.py: error: argument -s/--sprint_name: expected one argument
    ```

8. try option -m
 
    The `-m` markdown option:

    `go.bat "Sprint 123" "Sprint Goal A, B and C" -m`

    This formats the output using markdown notation.

9. try option -o

    The `-o` omit stretch issues option:

    `go.bat "Sprint 123" "Sprint Goal A, B and C" -o`

    This looks for a 'marker' issue that has summary containing text like `===`. Only issues that rank higher than this marker are included in the output.

1. (optional) get the text output to your clipboard, using the clip command line tool

   Simply append `| clip` to the command.

   Example:

   `go.bat "Sprint 123" "Sprint Goal A, B and C" | clip`

#### Example output

```
Sprint 123 - goal: Sprint Goal A, B and C
Done:
- [IP-1234] Implement feature X
- [IP-1235] Implement feature Y
In Progress:
- [IP-2001] Fix the button A
- [IP-2002] Fix the button B
To Do:
- [IP-2003] Fix the button C
- [IP-2004] Fix the button D
Dependencies/Impediments: None
```
