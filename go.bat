CALL set-jira-api-token-env-var.bat 

IF NOT EXIST temp (MKDIR temp)

REM Uses the default 'json' go-jira template
jira sprint-sos > temp\current-sprint-issues.json

python parse_current_sprint_issues.py -j temp\current-sprint-issues.json -s %1 -g %2 %3 %4
