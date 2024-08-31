import psycopg2
from psycopg2 import sql

def connect_to_postgresql(host, database, user, password):
    try:
        connection = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        print("Connection to PostgreSQL DB successful")
        return connection
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    conn = connect_to_postgresql("localhost", "mydatabase", "myuser", "mypassword")
    if conn:
        conn.close()