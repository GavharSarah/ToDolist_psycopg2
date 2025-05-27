from core.database_settings import execute_query

def add_task(name, quantity):
    query = """
    INSERT INTO TodoList1 (name, quantity)
    VALUES (%s, %s)
    """
    execute_query(query, params=(name, quantity))
    print("Task added successfully!")

def mark_task_complete(name):
    query = """
    UPDATE TodoList1 SET status = TRUE WHERE name = %s
    """
    execute_query(query, params=(name,))
    print(f"Task '{name}' marked as complete!")

def view_tasks():
    query = "SELECT * FROM TodoList1"
    tasks = execute_query(query, fetch="all")
    
    if tasks:
        for task in tasks:
            print(f"ID: {task[0]}, Name: {task[1]}, Details: {task[2]}, Completed: {'done' if task[3] else 'not done'}")
    else:
        print("No tasks found.")

