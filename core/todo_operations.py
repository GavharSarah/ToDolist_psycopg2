from core.database_settings import execute_query

def add_task(name, quantity):
    query = f"""
    INSERT INTO TodoList1 (name, quantity)
    VALUES ('{name}', '{quantity}')
    """
    execute_query(query)
    print("Task added successfully!")

def mark_task_complete(name):
    query = f"""
    UPDATE TodoList1 SET status = TRUE WHERE name = '{name}'
    """
    execute_query(query)
    print(f"Task '{name}' marked as complete!")

def view_tasks():
    query = "SELECT * FROM TodoList1"
    execute_query(query)

if __name__ == "__main__":
    add_task("Finish backend project", "Complete API integration")
    mark_task_complete("Finish backend project")
    view_tasks()
