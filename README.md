# taskOrganizer
A daily task management project
Task Organizer is a command-line tool (CLI) for managing tasks. The tool allows you to add tasks, list tasks, update task statuses, and export tasks to a CSV file.

## Requirements
- Python 3.6 or higher
- Additional modules: `argparse`, `json`, `tabulate`, `csv`

**Install dependencies**: Use the following command to install all required dependencies:
    ```bash
    pip install -r requirements.txt

 Use the `add` command to add a new task:
 python task_organizer.py add "Task Title" "Category" "date"   

  Use the `list` command to View all tasks:
 python task_organizer.py list 

  Use the `update` command to update task:
 python task_organizer.py update  
