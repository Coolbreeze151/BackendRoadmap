import pyodbc

def connect_to_mssql(server, database, user, password):
    try:
        connection = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={user};'
            f'PWD={password}'
        )
        print("Connection to MSSQL DB successful")
        return connection
    except Exception as e:
        print(f"Error: {e}")
        return None

def ingest_data_with_chunking(connection, table_name, data, chunk_size=1000):
    cursor = connection.cursor()
    for start in range(0, len(data), chunk_size):
        chunk = data[start:start + chunk_size]
        insert_query = f"INSERT INTO {table_name} VALUES (?, ?)"
        cursor.executemany(insert_query, chunk)
        connection.commit()
    cursor.close()

# Example usage
if __name__ == "__main__":
    conn = connect_to_mssql("localhost", "mydatabase", "myuser", "mypassword")
    if conn:
        # Assuming `data` is a list of tuples representing rows
        data = [(1, 'Alice'), (2, 'Bob'), ...]
        ingest_data_with_chunking(conn, "mytable", data)
        conn.close()