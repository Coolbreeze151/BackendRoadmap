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

# Example usage
if __name__ == "__main__":
    conn = connect_to_mssql("localhost", "mydatabase", "myuser", "mypassword")
    if conn:
        conn.close()