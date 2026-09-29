required_permissions = { 'Read', 'Write' }
employee_permissions = { 'Read', 'Write', 'Execute', 'Delete' }
print(employee_permissions.issuperset(required_permissions))
print(required_permissions.issubset(employee_permissions))