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

def ingest_data_with_chunking(connection, table_name, data, chunk_size=1000):
    cursor = connection.cursor()
    for start in range(0, len(data), chunk_size):
        chunk = data[start:start + chunk_size]
        insert_query = f"INSERT INTO {table_name} VALUES (%s, %s)"
        cursor.executemany(insert_query, chunk)
        connection.commit()
    cursor.close()

# Example usage
if __name__ == "__main__":
    conn = connect_to_mysql("localhost", "mydatabase", "myuser", "mypassword")
    if conn:
        # Assuming `data` is a list of tuples representing rows
        data = [(1, 'Alice'), (2, 'Bob'), ...]
        ingest_data_with_chunking(conn, "mytable", data)
        conn.close()