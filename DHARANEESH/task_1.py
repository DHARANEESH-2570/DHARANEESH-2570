# Simple To-Do List Application in Python

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nYour To-Do List:")
        for idx, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else "✗"
            print(f"{idx}. {task['task']} - [{status}]")

    def update_task(self, index, new_task):
        try:
            self.tasks[index]["task"] = new_task
            print("Task updated successfully.")
        except IndexError:
            print("Invalid task number.")

    def mark_task_completed(self, index):
        try:
            self.tasks[index]["completed"] = True
            print("Task marked as completed.")
        except IndexError:
            print("Invalid task number.")

    def delete_task(self, index):
        try:
            self.tasks.pop(index)
            print("Task deleted successfully.")
        except IndexError:
            print("Invalid task number.")

def main():
    todo = ToDoList()
    while True:
        print("\nTo-Do List Options:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            index = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter the updated task: ")
            todo.update_task(index, new_task)
        elif choice == "4":
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo.mark_task_completed(index)
        elif choice == "5":
            index = int(input("Enter task number to delete: ")) - 1
            todo.delete_task(index)
        elif choice == "6":
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
