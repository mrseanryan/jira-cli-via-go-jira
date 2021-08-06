CALL set-jira-api-token-env-var.bat 

jira sprint-sos > data\current-sprint-issues.json

python parse_current_sprint_issues.py -j data\current-sprint-issues.json -s "Sprint 44-BPs+Notfn+TA+(DPA)" -g "- MXP6 - L3 RELEASE - Fix LB Notifications - BPs - Test Automation - DPA (stretch) ?? Groom PB BPs - L1, L2 FREEZE LAST DAY OF SPRINT = 9.5.0" %1 %2 %3 %4
