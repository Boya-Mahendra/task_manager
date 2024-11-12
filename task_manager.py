import json

class Task:
    def _init_(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def mark_complete(self):
        """Marks the task as completed."""
        self.completed = True

    def to_dict(self):
        """Convert task to a dictionary for JSON serialization."""
        return {"id": self.id, "title": self.title, "completed": self.completed}

    @classmethod
    def from_dict(cls, task_data):
        """Create a Task instance from a dictionary."""
        return cls(task_data["id"], task_data["title"], task_data.get("completed", False))

    def _str_(self):
        status = "Completed" if self.completed else "Incomplete"
        return f"Task {self.id}: {self.title} [{status}]"


class TaskManager:
    def _init_(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
        self.next_id = self.get_next_id()

    def get_next_id(self):
        """Get the next ID incrementally based on the current list length."""
        return len(self.tasks) + 1

    def add_task(self, title):
        """Add a new task to the task list."""
        task = Task(task_id=self.next_id, title=title)
        self.tasks.append(task)
        self.next_id += 1
        print(f"Task '{title}' added with ID {task.id}.")

    def view_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for task in self.tasks:
                print(task)

    def delete_task(self, task_id):
        """Delete a task by its ID."""
        task_found = False
        self.tasks = [task for task in self.tasks if not (task_found := task.id == task_id)]
        
        if task_found:
            print(f"Task with ID {task_id} deleted.")
        else:
            print("Task not found.")

    def mark_task_complete(self, task_id):
        """Mark a task as completed."""
        for task in self.tasks:
            if task.id == task_id:
                task.mark_complete()
                print(f"Task '{task.title}' marked as completed.")
                return
        print("Task not found.")

    def save_tasks(self):
        """Save tasks to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)
        print("Tasks saved to tasks.json.")

    def load_tasks(self):
        """Load tasks from a JSON file if it exists."""
        try:
            with open(self.filename, 'r') as file:
                self.tasks = [Task.from_dict(data) for data in json.load(file)]
            print(f"Loaded {len(self.tasks)} tasks from {self.filename}.")
        except FileNotFoundError:
            print(f"No existing task file found. Starting fresh.")
            self.tasks = []

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Save Tasks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter the task title: ")
            task_manager.add_task(title)
        elif choice == "2":
            task_manager.view_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to delete: "))
                task_manager.delete_task(task_id)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                task_manager.mark_task_complete(task_id)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            task_manager.save_tasks()
        elif choice == "6":
            task_manager.save_tasks()
            print("Exiting the Task Manager.")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "_main_":
    main()
