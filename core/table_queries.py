

from core.database_settings import execute_query

TodoList1 = """
CREATE TABLE IF NOT EXISTS TodoList1 (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) NOT NULL UNIQUE,
    quantity VARCHAR(128) NOT NULL,
    status BOOLEAN DEFAULT FALSE
);
"""

def initializing_tables():
    execute_query(TodoList1)

if __name__ == "__main__":
    initializing_tables()
    print("To-Do table created successfully!")
