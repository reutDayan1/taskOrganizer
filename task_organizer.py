import argparse
import csv
import json
from datetime import datetime
from tabulate import tabulate

TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Add a new task
def add_task(tasks, title, category, due_date):
    task = {
        "title": title,
        "category": category,
        "due_date": due_date,
        "status": "Pending"
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

# List tasks
def list_tasks(tasks, filter_category=None, show_completed=False):
    filtered_tasks = [
        t for t in tasks
        if (filter_category is None or t["category"] == filter_category) and
        (show_completed or t["status"] == "Pending")
    ]
    print(tabulate(filtered_tasks, headers="keys", tablefmt="grid"))

# Update task status
def update_task_status(tasks, title, status):
    for task in tasks:
        if task["title"] == title:
            task["status"] = status
            save_tasks(tasks)
            print(f"Task '{title}' updated to {status}!")
            return
    print(f"Task '{title}' not found!")

# Export tasks to CSV
def export_tasks(tasks, filename):
    keys = tasks[0].keys() if tasks else []
    with open(filename, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(tasks)
    print(f"Tasks exported to {filename} successfully!")

# Main function
def main():
    parser = argparse.ArgumentParser(description="Task Organizer")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Add task command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("category", help="Task category")
    add_parser.add_argument("due_date", help="Due date (YYYY-MM-DD)")

    # List tasks command
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("--category", help="Filter by category")
    list_parser.add_argument("--show-completed", action="store_true", help="Include completed tasks")

    # Update task status command
    update_parser = subparsers.add_parser("update", help="Update task status")
    update_parser.add_argument("title", help="Task title")
    update_parser.add_argument("status", choices=["Pending", "Completed"], help="New status")

    # Export tasks command
    export_parser = subparsers.add_parser("export", help="Export tasks to a CSV file")
    export_parser.add_argument("filename", help="CSV file name to export tasks")

    args = parser.parse_args()
    tasks = load_tasks()

    if args.command == "add":
        add_task(tasks, args.title, args.category, args.due_date)
    elif args.command == "list":
        list_tasks(tasks, args.category, args.show_completed)
    elif args.command == "update":
        update_task_status(tasks, args.title, args.status)
    elif args.command == "export":
        export_tasks(tasks, args.filename)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()