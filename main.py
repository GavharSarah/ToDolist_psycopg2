from core.database_settings import execute_query
from core.table_queries import initializing_tables


def main():
    params = (12,)
    query = "select * from users"
    execute_query(query=query, params=params, fetch="all")


if __name__ == '__main__':
    initializing_tables()
    main()
