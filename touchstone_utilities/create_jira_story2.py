from jira import JIRA

# Jira connection
jira_server = 'https://voereir.atlassian.net'
jira_user = 'isar@voereir.com'
jira_token = 'ATATT3xFfGF0z9zKtjCbPRLD_zYMbNJcpMghAmXHK17HkqTPO2Q0DlWvyCk5-LDpZhc4bMlZIvYWkFvPuSV9UYUQLa-FkG_lsyyRNMXiFL_OLKOSzl-liGKm7OLR5nFmqNz4cpEacwTEQ6Z15jwrkul4luptkNQsp2RcPLkh46ti4O7KiVCK_Tg=0443A6F0'  # Generate from Atlassian account

options = {"server": jira_server}
jira = JIRA(options, basic_auth=(jira_user, jira_token))

# Story details
issue_dict = {
    'project': {'key': 'VOER'},  # Replace with your project key
    'summary': 'New story created via API',
    'parent': {'key': 'VOER-2195'},
    'description': 'This task was created using Python and Jira API.',
    'issuetype': {'name': 'Task'},
    'labels': ['automated'],
    'priority': {'name': 'Medium'},
    'components': [{'name': 'QA Automation'}]
}

# Create the issue
new_issue = jira.create_issue(fields=issue_dict)

print(f"Issue {new_issue.key} created successfully.")

