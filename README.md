# Jira cmd line README

## Ref

https://github.com/go-jira/jira

## Usage

### Login

1. create API token via the Jira website

2. configure Go-Jira (see ref section above) for endpoint, user, project - this is the `.jira-d/config.yml` file

3. create a script to set JIRA_API_TOKEN

set-jira-api-token-env-var.bat
```
@ECHO OFF
SET JIRA_API_TOKEN={token value}
```

4. login

`jira session`

### Read data from JIRA

5. run the test script (it is only reading, not writing!)

This is to check everything is setup OK.

This script dumps a text report of the current sprint status, with stories + bugs ranked and grouped by status.

`test_dump_current_sprint_state_sos.bat`

6. see the available options

`go.bat`

```
usage: parse_current_sprint_issues.py [-h] -j JSON -s SPRINT_NAME -g GOAL [-o]
parse_current_sprint_issues.py: error: argument -s/--sprint_name: expected one argument
```

7. try other options

`go.bat "Sprint 123" "Sprint Goal A, B and C" -o`

note: `-o` looks for a 'marker' issue that has summary containing text like `===`. Only issues that rank higher than this marker are included in the output.
