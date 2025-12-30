# Terminal Todo List

A minimalistic, lightweight command-line interface (CLI) to-do list manager that stores your tasks in a local JSON file. It's perfect for developers who want to manage tasks without leaving their terminal.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Simple file-based storage**: Tasks are saved to `todos.json` in the script directory.
*   **Zero Dependencies**: Uses only the Python standard library.
*   **CRUD Operations**: Add, list, complete, and delete tasks easily.

## Usage

```bash
python run_todo.py [command] [options]
```

### Commands

*   `add "Task Name"`: Create a new task.
*   `list`: Show pending tasks.
*   `list --all`: Show all tasks, including completed ones.
*   `done [ID]`: Mark a task as completed by its ID.
*   `del [ID]`: Delete a task forever.
*   `clear`: Remove all completed tasks to clean up the list.

### Examples

**1. Adding Tasks**
```bash
python run_todo.py add "Finish the report"
python run_todo.py add "Buy milk"
```

**2. Listing Tasks**
```bash
python run_todo.py list
```
Output:
```
ID    Status     Task
----------------------------------------
1     [ ]        Finish the report
2     [ ]        Buy milk
----------------------------------------
```

**3. Completing a Task**
```bash
python run_todo.py done 1
```

**4. Cleaning Up**
```bash
python run_todo.py clear
```

## Installation

No installation required. Clone the repo and run with Python 3.

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
