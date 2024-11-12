Class TaskManager
This class manages a list of tasks and handles operations like adding, deleting, viewing, and saving tasks.

_init_(self, filename="tasks.json"): Initializes the task manager, loading tasks from tasks.json if it exists and setting the next task ID.
get_next_id(self): Determines the next task ID incrementally.
add_task(self, title): Adds a new task with the provided title.
view_tasks(self): Displays all tasks in the console.
delete_task(self, task_id): Deletes a task based on its ID. If the ID isn’t found, it notifies the user.
mark_task_complete(self, task_id): Marks a specified task as completed if it exists.
save_tasks(self): Saves the list of tasks to tasks.json in JSON format.
load_tasks(self): Loads tasks from tasks.json if it exists. If not, it initializes an empty task list.
main() Function
The main() function starts the Task Manager program and provides a menu-based interface for the user to interact with.

Displays Options:

Add Task
View Tasks
Delete Task
Mark Task as Completed
Save Tasks
Exit (which also saves tasks automatically)
Processes User Choice:

Based on the user’s input, it calls the appropriate method in the TaskManager class.
Error Handling:

If an invalid option is entered, it asks the user to choose again.
Uses try-except to handle invalid input when expecting numeric task IDs.
Key Functions Explained
Adding a Task: Asks the user for a task title, creates a new task, and appends it to the list.
Viewing Tasks: Displays all tasks, showing the ID, title, and whether each task is completed.
Deleting a Task: Prompts for the task ID and removes it from the list if found.
Marking a Task Complete: Prompts for the task ID and marks it as completed.
Saving Tasks: Converts each task to a dictionary and writes them to tasks.json in JSON format.
Loading Tasks: Reads from tasks.json, reconstructs each task as a Task object, and loads them into the list.
Running the Program
Start the program by running the python task_manager.py command.
Choose an option from the menu by entering the number associated with the action you want (1 to 6).
When you add, delete, or mark tasks as complete, the list of tasks is updated.
Choosing "Save Tasks" (option 5) will save any changes to tasks.json.
Choosing "Exit" (option 6) will save tasks and end the program.