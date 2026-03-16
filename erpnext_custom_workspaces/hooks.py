app_name = "erpnext_custom_workspaces"
app_title = "ERPNext Custom Workspaces"
app_publisher = "My Company"
app_description = "Custom Workspaces for ERPNext"
app_email = "ph.tamir@gmail.com"
app_license = "MIT"

fixtures = [
    {
        "dt": "Workspace",
        "filters": [
            ["module", "=", "Custom Workspaces"]
        ]
    },
    {
        "dt": "Role",
        "filters": [
            ["name", "in", ["My Company Operations Manager", "My Company Sales Manager", "My Company Accounts Manager"]]
        ]
    }
]