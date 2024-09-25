from cassandra.cluster import Cluster

def create_keyspace():
    cluster = Cluster(['localhost'])  # Replace 'localhost' with your Cassandra cluster address
    session = cluster.connect()

    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS my_keyspace
        WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
    """)

    session.set_keyspace('my_keyspace')

def create_table():
    cluster = Cluster(['localhost'])  # Replace 'localhost' with your Cassandra cluster address
    session = cluster.connect()

    session.execute("""
        CREATE TABLE IF NOT EXISTS my_table (
            id UUID PRIMARY KEY,
            name TEXT,
            age INT
        )
    """)

if __name__ == '__main__':
    create_keyspace()
    create_table()