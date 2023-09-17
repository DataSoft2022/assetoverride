import frappe
from erpnext.assets.doctype.asset_maintenance_log.asset_maintenance_log import AssetMaintenanceLog
from erpnext.assets.doctype.asset_maintenance.asset_maintenance import AssetMaintenance
  
import datetime
import json
class CustomAsset(AssetMaintenanceLog):
    def validate(self):
        pass
        
       
class CustomAssetMain(AssetMaintenance):
    def validate(self):
        pass
    
    def on_update(self):
        pass
       


@frappe.whitelist()
def onAddAsset(frm_name, table):
    for task in json.loads(table):
        print("\n\n\n\n\n\n\n", task, "\n\\n\n\n\n\n\n")
        if task["cumulative_hours_till_now"] == '0':
            item = frappe.new_doc('Asset Maintenance Log');
            item.asset_maintenance =  frm_name;
            item.task = task["name"];
            item.task_name =  task["task"];
            item.completion_date = datetime.datetime.now().date()
            item.assign_to_name = task['assign_to']
            #item.item_code = task["item_code"];
            #item.item_name = task["item_name"];
            item.maintenance_status = 'Planned';
            item.due_date = task.get('due_date')
            item.insert()
            print("\n\n\n\n\n\n\n", item, "\n\\n\n\n\n\n\n")
    frappe.db.commit()
