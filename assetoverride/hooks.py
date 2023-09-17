from . import __version__ as app_version

app_name = "assetoverride"
app_title = "Assetoverride"
app_publisher = "asdf"
app_description = "asdf"
app_icon = "sd"
app_color = "grey"
app_email = "sd"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/assetoverride/css/assetoverride.css"
# app_include_js = "/assets/assetoverride/js/assetoverride.js"

# include js, css files in header of web template
# web_include_css = "/assets/assetoverride/css/assetoverride.css"
# web_include_js = "/assets/assetoverride/js/assetoverride.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "assetoverride/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "assetoverride.install.before_install"
# after_install = "assetoverride.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "assetoverride.uninstall.before_uninstall"
# after_uninstall = "assetoverride.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "assetoverride.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
        "Asset Maintenance Log": "assetoverride.overrides.overrides.CustomAsset",
        "Asset Maintenance": "assetoverride.overrides.overrides.CustomAssetMain"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"assetoverride.tasks.all"
# 	],
# 	"daily": [
# 		"assetoverride.tasks.daily"
# 	],
# 	"hourly": [
# 		"assetoverride.tasks.hourly"
# 	],
# 	"weekly": [
# 		"assetoverride.tasks.weekly"
# 	]
# 	"monthly": [
# 		"assetoverride.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "assetoverride.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "assetoverride.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "assetoverride.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"assetoverride.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
