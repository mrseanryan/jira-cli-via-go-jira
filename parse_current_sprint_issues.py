import argparse
import json

ap = argparse.ArgumentParser()
ap.add_argument("-j", "--json", required=True,
                help="Path to JSON file")
ap.add_argument("-s", "--sprint_name", required=True,
                help="The name of the sprint")
ap.add_argument("-g", "--goal", required=True,
                help="The sprint goal")
ap.add_argument("-o", "--omit_stretch",  action='store_true', required=False,
                help="Omit stretch issues")

args = vars(ap.parse_args())

path_to_json = args['json']
sprint_name = args['sprint_name']
sprint_goal = args['goal']
omit_stretch_issues = args['omit_stretch']

with open(path_to_json) as f:
    data = json.load(f)

def convert_json_issue(i):
    return {"key": i['key'], "type": i['fields']['issuetype']['name'], "priority": i['fields']['priority']['name'], "status": i['fields']['status']['name'], "summary": i['fields']['summary']}

# Assumption: issues already sorted by rank
# (rank is not in the JSON - so we calculate index, so we can keep sorting by rank)
indexed_issue_dump = [{'issue':convert_json_issue(x), 'rank':i} for i,x in enumerate(data['issues'])]

def flatten_indexed_issue(i):
  flattened = i['issue']
  flattened['rank'] = i['rank']
  return flattened
 
issue_dump = list(map(flatten_indexed_issue, indexed_issue_dump))

# print(issue_dump)

issue_dump_before_stretch = []
found_stretch_marker = False
for issue in issue_dump:
  if ("===" in issue['summary']):
    found_stretch_marker = True
  if not(found_stretch_marker):
    issue_dump_before_stretch.append(issue)

active_issue_dump = issue_dump
if (omit_stretch_issues):
  active_issue_dump = issue_dump_before_stretch

def zero_pad(n):
  return f'{n:08}'

def sort_issues(issues):
  return sorted(issues, key=lambda x: zero_pad(x['rank']) + x['status'] + x['priority'] + x['type'])

sorted_issue_dump = sort_issues(active_issue_dump)

# - add header for sprint goal (not available via the go-jira tool)
print(f"{sprint_name} - goal: {sprint_goal}")

statuses = set(map(lambda x: x['status'], sorted_issue_dump))

def dump_issue(issue):
  print(f"- [{issue['key']}] {issue['summary']}")

for status in sorted(statuses):
  print(f"{status}:")
  issues_this_status = sort_issues(filter(lambda i: i['status'] == status, sorted_issue_dump))
  for issue in issues_this_status:
    dump_issue(issue)

# - add footer for deps/impeds
print("Dependencies/Impediments: None")
