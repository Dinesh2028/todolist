import sqlite3

# Establish database connection
conn = sqlite3.connect("todo_list.db")
cursor = conn.cursor()

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            status TEXT CHECK(status IN ('Pending', 'Completed')) NOT NULL DEFAULT 'Pending'
        )
    """)
    conn.commit()

def add_task(title):
    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    print("Task added successfully!")

def view_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    if tasks:
        print("\nTo-Do List:")
        for task in tasks:
            print(f"ID: {task[0]}, Title: {task[1]}, Status: {task[2]}")
    else:
        print("No tasks found!")

def update_task(task_id, new_title):
    cursor.execute("UPDATE tasks SET title=? WHERE id=?", (new_title, task_id))
    conn.commit()
    if cursor.rowcount > 0:
        print("Task updated successfully!")
    else:
        print("Task not found!")

def mark_completed(task_id):
    cursor.execute("UPDATE tasks SET status='Completed' WHERE id=?", (task_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print("Task marked as completed!")
    else:
        print("Task not found!")

def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print("Task deleted successfully!")
    else:
        print("Task not found!")

if __name__ == "__main__":
    create_table()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to update: "))
                new_title = input("Enter new title: ")
                update_task(task_id, new_title)
            except ValueError:
                print("Invalid input! Task ID must be a number.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                mark_completed(task_id)
            except ValueError:
                print("Invalid input! Task ID must be a number.")
        elif choice == "5":
            try:
                task_id = int(input("Enter task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Invalid input! Task ID must be a number.")
        elif choice == "6":
            print("Exiting...")
            conn.close()
            break
        else:
            print("Invalid choice! Try again.")
