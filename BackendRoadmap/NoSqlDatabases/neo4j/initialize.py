from neo4j import GraphDatabase

# Connect to the Neo4j database
uri = "bolt://localhost:7687"
username = "your_username"
password = "your_password"
driver = GraphDatabase.driver(uri, auth=(username, password))

# Define the Cypher query to create nodes and relationships
cypher_query = """
CREATE (person:Person {name: 'John'})
CREATE (person)-[:FRIEND]->(friend:Person {name: 'Jane'})
"""

# Execute the Cypher query
with driver.session() as session:
    session.run(cypher_query)

# Close the database connection
driver.close()