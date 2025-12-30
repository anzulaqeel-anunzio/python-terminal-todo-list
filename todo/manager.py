# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import json
import os
from datetime import datetime

class TodoManager:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = self.load_todos()

    def load_todos(self):
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []

    def save_todos(self):
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f, indent=4)

    def add_task(self, task):
        new_id = 1
        if self.todos:
            new_id = max(t['id'] for t in self.todos) + 1
        
        new_task = {
            "id": new_id,
            "task": task,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.todos.append(new_task)
        self.save_todos()
        print(f"Task added: [{new_id}] {task}")

    def list_tasks(self, show_all=False):
        if not self.todos:
            print("No tasks found.")
            return

        print(f"\n{'ID':<5} {'Status':<10} {'Task'}")
        print("-" * 40)
        for t in self.todos:
            if t['completed'] and not show_all:
                continue
            status = "[x]" if t['completed'] else "[ ]"
            print(f"{t['id']:<5} {status:<10} {t['task']}")
        print("-" * 40)

    def complete_task(self, task_id):
        for t in self.todos:
            if t['id'] == task_id:
                t['completed'] = True
                self.save_todos()
                print(f"Task {task_id} marked as completed.")
                return
        print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        initial_len = len(self.todos)
        self.todos = [t for t in self.todos if t['id'] != task_id]
        if len(self.todos) < initial_len:
            self.save_todos()
            print(f"Task {task_id} deleted.")
        else:
            print(f"Task with ID {task_id} not found.")

    def clear_completed(self):
        self.todos = [t for t in self.todos if not t['completed']]
        self.save_todos()
        print("Cleared all completed tasks.")

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
