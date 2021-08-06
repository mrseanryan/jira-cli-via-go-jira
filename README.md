# Jira cmd line README

## Ref

https://github.com/go-jira/jira

## Notes

### Login

1. create API token via the Jira website

2. configure Go-Jira (see ref) for endpoint, user, project - this is the .jira-d/config.yml file

3. create a script to set JIRA_API_TOKEN

set-jira-api-token-env-var.bat
```
@ECHO OFF
SET JIRA_API_TOKEN={token value}
```

4. login

`jira session`

