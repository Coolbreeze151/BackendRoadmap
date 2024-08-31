import psycopg2
import pandas as pd

def ingest_data_with_chunking(connection, table_name, data, chunk_size=1000):
    cursor = connection.cursor()
    for start in range(0, len(data), chunk_size):
        chunk = data[start:start + chunk_size]
        insert_query = sql.SQL("INSERT INTO {} VALUES %s").format(sql.Identifier(table_name))
        psycopg2.extras.execute_values(cursor, insert_query, chunk)
        connection.commit()
    cursor.close()

# Example usage
if __name__ == "__main__":
    conn = connect_to_postgresql("localhost", "mydatabase", "myuser", "mypassword")
    if conn:
        # Assuming `data` is a list of tuples representing rows
        data = [(1, 'Alice'), (2, 'Bob'), ...]
        ingest_data_with_chunking(conn, "mytable", data)
        conn.close()