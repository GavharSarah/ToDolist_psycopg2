
from core.database_settings import execute_query
from core.table_queries import initializing_tables
from core.todo_operations import add_task, mark_task_complete, view_tasks



def main():
    initializing_tables()  

    while True:
        action = input("Enter 'add', 'complete', 'view', or 'exit': ").strip().lower()

        if action == "add":
            name = input("Task name: ")
            quantity = input("Details: ")
            add_task(name, quantity)

        elif action == "complete":
            name = input("Task to mark complete: ")
            mark_task_complete(name)

        elif action == "view":
            view_tasks()

        elif action == "exit":
            print("Goodbye!")
            break

        else:
            print("Invalid action! Please enter 'add', 'complete', 'view', or 'exit'.")

if __name__ == '__main__':
    main()




