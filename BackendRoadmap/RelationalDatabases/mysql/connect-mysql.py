import mysql.connector
from mysql.connector import Error

def connect_to_mysql(host, database, user, password):
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    conn = connect_to_mysql("localhost", "mydatabase", "myuser", "mypassword")
    if conn:
        conn.close()