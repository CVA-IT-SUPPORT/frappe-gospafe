# -*- coding: utf-8 -*-
# Copyright (c) 2019, GOSPAFE and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import frappe
from frappe import _
# import frappe
from frappe.model.document import Document


class Project(Document):

        def onload(self):
                """Load project tasks for quick view"""
                frappe.msgprint("Hello on Load")
                if not self.get('__unsaved') and not self.get("tasks"):
                        self.load_tasks()

        def before_print(self):
                self.onload()

        def load_tasks(self):
                frappe.msgprint("on load_tasks")
                """Load `tasks` from the database"""
                project_task_custom_fields = frappe.get_all("Custom Field", {"dt": "Project Task"}, "fieldname")
                #frappe.msgprint(project_task_custom_fields)
                frappe.msgprint("on project task custom field")
                #frappe.msgprint(vars(project_task_custom_fields))
                frappe.errprint("your message")

                self.tasks = []
                for task in self.get_tasks():
                        task_map = {
                                "title": task.subject,
                                "status": task.status,
                                "start_date": task.start_date,
                                "end_date": task.end_date,
                                "description": task.description,
                                "task_id": task.name,
                                "task_weight": task.task_weight
                        }

                        self.map_custom_fields(task, task_map, project_task_custom_fields)

                        self.append("project_task", task_map)

        def get_tasks(self):
                if self.name is None:
                        return {}
                else:
                        filters = {"project": self.name}

                        if self.get("deleted_task_list"):
                                filters.update({
                                        'name': ("not in", self.deleted_task_list)
                                })

                        return frappe.get_all("Task", "*", filters, order_by="start_date asc, status asc")

        def map_custom_fields(self, source, target, custom_fields):
                for field in custom_fields:
                        target.update({
                                field.fieldname: source.get(field.fieldname)
                        })
