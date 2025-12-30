# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from todo.manager import TodoManager

def main():
    parser = argparse.ArgumentParser(description="A simple terminal-based Todo List")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", help="The task description")

    # List command
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("--all", "-a", action="store_true", help="Show all tasks including completed")

    # Done command
    done_parser = subparsers.add_parser("done", help="Mark a task as completed")
    done_parser.add_argument("id", type=int, help="Task ID")

    # Delete command
    del_parser = subparsers.add_parser("del", help="Delete a task")
    del_parser.add_argument("id", type=int, help="Task ID")

    # Clear command
    subparsers.add_parser("clear", help="Clear all completed tasks")

    args = parser.parse_args()

    # Default file path is in the same directory as the script
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todos.json")
    manager = TodoManager(json_path)

    if args.command == "add":
        manager.add_task(args.task)
    elif args.command == "list":
        manager.list_tasks(show_all=args.all)
    elif args.command == "done":
        manager.complete_task(args.id)
    elif args.command == "del":
        manager.delete_task(args.id)
    elif args.command == "clear":
        manager.clear_completed()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
