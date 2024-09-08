import json

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = '✓' if self.completed else '✗'
        return f"{status} {self.description}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def list_tasks(self):
        return [str(task) for task in self.tasks]

    def update_task(self, index, description=None, completed=None):
        if 0 <= index < len(self.tasks):
            if description is not None:
                self.tasks[index].description = description
            if completed is not None:
                self.tasks[index].completed = completed

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump([task.__dict__ for task in tasks], file)

def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            task_dicts = json.load(file)
            tasks = [Task(**task_dict) for task_dict in task_dicts]
            return tasks
    except FileNotFoundError:
        return []

def display_tasks(task_manager):
    tasks = task_manager.list_tasks()
    for i, task in enumerate(tasks):
        print(f"{i}. {task}")

def main():
    task_manager = TaskManager()
    task_manager.tasks = load_tasks('tasks.json')

    while True:
        print("\nTo-Do List:")
        display_tasks(task_manager)

        print("\nOptions:")
        print("1. Add task")
        print("2. Update task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            task_manager.add_task(description)
        elif choice == '2':
            index = int(input("Enter task number to update: "))
            new_description = input("Enter new description (leave empty to keep current): ")
            completed = input("Mark as completed? (y/n): ").lower() == 'y'
            task_manager.update_task(index, new_description, completed)
        elif choice == '3':
            index = int(input("Enter task number to delete: "))
            task_manager.delete_task(index)
        elif choice == '4':
            save_tasks('tasks.json', task_manager.tasks)
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
