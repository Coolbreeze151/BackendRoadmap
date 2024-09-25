### [Back Home](../../README.md)

# NoSQL Databases

## Table of Contents

- [Introduction](#introduction)
- [What is NoSQL Databases](#what-is-nosql-databases)
- [Advantages & Disadvantages](#advantages--disadvantages)
    - [Advantages](#advantages)
    - [Disadvantages](#disadvantages)
- [Graph DBs](#graph-dbs)
- [Column DBs](#column-dbs)
- [Time Series DBs](#time-series-dbs)
- [Real-Time DBs](#real-time-dbs)
- [Document DBs](#document-dbs)
- [Key-Value DBs](#key-value-dbs)
- [Examples](#examples)

## Introduction
NoSQL databases are a category of database management systems designed to handle unstructured or semi-structured data. Unlike traditional relational databases, NoSQL databases are schema-less and offer flexible data models for distributed and large-scale applications. They provide a variety of models to accommodate different data storage requirements, enabling faster and more scalable solutions for modern applications.

## What is NoSQL Databases

NoSQL (Not Only SQL) databases are built to manage vast amounts of unstructured data and scale horizontally across distributed systems. They allow for dynamic schema design, making them more adaptable to changing data structures and accommodating varying data types. NoSQL databases fall into multiple categories based on how data is modeled, including document, key-value, column-family, graph, and time-series databases.

## Key characteristics of NoSQL databases:

- Schema-less design.
- High scalability.
- Support for distributed, large-scale data storage.
- Horizontal scaling via partitioning and replication.

Common use cases for NoSQL databases include real-time web apps, IoT data management, social networks, and large-scale content management systems.

## Advantages & Disadvantages

### Advantages

- Scalability: NoSQL databases are designed to scale horizontally, allowing easy expansion across multiple servers.
- Flexibility: They provide flexible data models, enabling the handling of unstructured and semi-structured data.
- Performance: NoSQL databases can process large volumes of data quickly, making them ideal for real-time applications.
- Availability: With built-in replication and distribution across nodes, NoSQL databases often offer high availability and fault tolerance.
- Cost-effective: Scaling with commodity hardware reduces costs in comparison to traditional databases that rely on high-performance single servers.

### Disadvantages

- Lack of ACID Compliance: Many NoSQL databases sacrifice ACID properties (Atomicity, Consistency, Isolation, Durability) for scalability, which can lead to eventual consistency models.
- Complexity in Querying: Unlike SQL with its well-defined query language, NoSQL databases often use less mature querying mechanisms.
- Learning Curve: Developers may find NoSQL databases challenging due to the lack of standardized query languages or interfaces across different NoSQL systems.
- Less Mature Ecosystem: Compared to relational databases, the NoSQL ecosystem can be less robust in terms of tools, libraries, and best practices.

## Graph DBs

Graph databases are designed to handle relationships between data points. They store data in nodes, edges, and properties, making them ideal for use cases where relationships and connections between entities are central.

- Data Model: Nodes (entities), Edges (relationships), Properties (key-value pairs).
- Use Cases: Social networks, recommendation engines, fraud detection, network management.
- Examples: Neo4j, Amazon Neptune, OrientDB.

### Advantages:

- Efficiently manages highly interconnected data.
- Flexible querying with traversal-based algorithms.

### Disadvantages:

- Not ideal for bulk analytics or simple key-value lookups.
- Limited to specific relationship-driven use cases.

## Column DBs

Column-family databases are designed to store data in columns rather than rows, optimizing for read and write operations on large datasets. They are particularly effective for data warehousing and high-volume transactional systems.

- Data Model: Tables with rows and columns, but data is stored by columns rather than rows.
- Use Cases: Analytics, time-series data, large-scale transactional systems.
- Examples: Apache Cassandra, HBase, ScyllaDB.

### Advantages:

- Optimized for read-heavy operations.
- Scalable and fault-tolerant with distributed architecture.

### Disadvantages:

- Higher complexity in managing schema and data models.
- Inconsistent reads in some implementations (eventual consistency).

## Time Series DBs

Time series databases are optimized for the collection, storage, and retrieval of time-stamped or time-interval-based data. They are used to manage metrics, events, and sensor data efficiently.

- Data Model: Time-stamped events stored with associated metadata.
- Use Cases: Monitoring systems, IoT data, financial data, real-time analytics.
- Examples: InfluxDB, TimescaleDB, OpenTSDB.

### Advantages:

- Efficient querying and storage of time-based data.
- Advanced features for data compression and downsampling.

### Disadvantages:

- Not designed for complex relational data.
- Limited use cases outside of time-series analytics.

## Real-Time DBs

Real-time databases are designed to handle data that needs to be processed and queried instantly. These databases are optimized for low-latency operations, often supporting high-throughput ingestion.

- Data Model: Real-time streams of data with immediate processing and querying.
- Use Cases: Financial trading, real-time analytics, fraud detection, IoT.
- Examples: Redis, Aerospike, Memcached.

### Advantages:

- Low-latency operations.
- Optimized for high read/write throughput.

### Disadvantages:

- Memory-intensive, may require high hardware resources.
- Limited use cases centered around real-time data needs.

## Document DBs

Document databases store and retrieve data in document format, typically using JSON, BSON, or XML. They allow for flexible data models where each document can have a different structure, making them ideal for storing semi-structured data.

- Data Model: Documents (typically JSON or BSON), stored in collections.
- Use Cases: Content management systems, mobile apps, catalogs, web applications.
- Examples: MongoDB, CouchDB, Firebase.

### Advantages:

- Flexible schema with dynamic and semi-structured data.
- Easy to scale horizontally with built-in sharding and replication.

### Disadvantages:

- Inefficient for highly relational data.
- Lack of advanced querying features found in SQL-based systems.

## Key-Value DBs

Key-value databases are among the simplest NoSQL databases, storing data as a collection of key-value pairs. They are extremely fast for lookup operations and are often used for caching or session management.

- Data Model: Key-value pairs (keys are unique, values can be any data type).
- Use Cases: Caching, session management, configuration data storage, real-time analytics.
- Examples: Redis, DynamoDB, Riak.

### Advantages:

- Simple and highly performant for specific use cases.
- Horizontal scalability with high availability.

### Disadvantages:

- Limited querying capability (only by key).
- Inefficient for complex or relational data needs.


### Examples
Refer to list of example NoSQL Database here for more details

| Type           | Example |
|----------------|---------|
| Document DBs   |[Mongo DB](./mongodb/readme.md)         |
| Key-Value DBs  |[Redis](./redis/readme.md)         |
| Column DBs     |[Cassandra]()         |
| Graph DBs      | [Neo4J](./neo4j/readme.md)        |
| Time Series DBs|[Influx DB]()         |
| Real-Time DBs  |[Firebase]()         |

[Back to top](#top)