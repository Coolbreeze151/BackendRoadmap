### [Back Home](../../README.md)
# More about Databases

This repository contains additional information topics related to databases.

## Table of Contents

- [ORMs](#orms)
- [ACID](#acid)
- [Transactions](#transactions)
- [N+1 Problem](#n1-problem)
- [Normalizations](#normalizations)
- [Failure Modes](#failure-modes)
- [Profiling Performance](#profiling-performance)

## [ORMs](https://stackoverflow.com/questions/1279613/what-is-an-orm-how-does-it-work-and-how-should-i-use-one/1279678#1279678)

Object-Relational Mapping (ORM) is a programming technique that allows developers to interact with a relational database using object-oriented programming concepts. ORM frameworks map database tables to classes and rows to objects, enabling developers to perform database operations through objects rather than writing raw SQL queries. This abstraction simplifies data manipulation and improves code maintainability by aligning database interactions with the application’s object model. ORM tools handle the translation between objects and database schemas, manage relationships, and often provide features like lazy loading and caching. Popular ORM frameworks include Hibernate for Java, Entity Framework for .NET, and SQLAlchemy for Python.

## [ACID](https://retool.com/blog/whats-an-acid-compliant-database)

ACID is an acronym representing four key properties that guarantee reliable processing of database transactions. It stands for Atomicity, Consistency, Isolation, and Durability. Atomicity ensures that a transaction is treated as a single, indivisible unit that either completes entirely or fails completely. Consistency maintains the database in a valid state before and after the transaction. Isolation ensures that concurrent transactions do not interfere with each other, appearing to execute sequentially. Durability guarantees that once a transaction is committed, it remains so, even in the event of system failures. These properties are crucial in maintaining data integrity and reliability in database systems, particularly in scenarios involving multiple, simultaneous transactions or where data accuracy is critical, such as in financial systems or e-commerce platforms.

## [Transactions](https://fauna.com/blog/database-transaction)

In database systems, a transaction is a series of operations that are executed as a single, atomic unit to ensure data integrity and consistency. Transactions adhere to the ACID properties: Atomicity ensures all operations complete successfully or none are applied; Consistency maintains the database’s valid state; Isolation prevents transactions from interfering with each other; and Durability guarantees that once a transaction is committed, its changes are permanent. These properties collectively ensure that databases handle concurrent operations reliably and maintain accurate and consistent data even in the face of failures.

## [N+1 Problem](https://medium.com/doctolib/understanding-and-fixing-n-1-query-30623109fe89)

The N+1 problem occurs in database querying when an application performs a query to retrieve a list of items and then issues additional queries to fetch related data for each item individually. This often results in inefficiencies and performance issues because the number of queries issued grows proportionally with the number of items retrieved. For example, if an application retrieves 10 items and then performs an additional query for each item to fetch related details, it ends up executing 11 queries (1 for the list and 10 for the details), leading to a total of 11 queries instead of 2. This can severely impact performance, especially with larger datasets. Solutions to the N+1 problem typically involve optimizing queries to use joins or batching techniques to retrieve related data in fewer, more efficient queries.

## [Normalizations](https://www.guru99.com/database-normalization.html)

Database normalization is the process of structuring a relational database in accordance with a series of so-called normal forms in order to reduce data redundancy and improve data integrity. It was first proposed by Edgar F. Codd as part of his relational model. Normalization entails organizing the columns (attributes) and tables (relations) of a database to ensure that their dependencies are properly enforced by database integrity constraints. It is accomplished by applying some formal rules either by a process of synthesis (creating a new database design) or decomposition (improving an existing database design).



## Failure Modes

Database failure modes refer to the various ways in which a database system can malfunction or cease to operate correctly. These include hardware failures (like disk crashes or network outages), software bugs, data corruption, performance degradation due to overload, and inconsistencies in distributed systems. Common failure modes involve data loss, system unavailability, replication lag in distributed databases, and deadlocks. To mitigate these, databases employ strategies such as redundancy, regular backups, transaction logging, and failover mechanisms. Understanding potential failure modes is crucial for designing robust database systems with high availability and data integrity. It informs the implementation of fault tolerance measures, recovery procedures, and monitoring systems to ensure database reliability and minimize downtime in critical applications.

## [Profiling Performance](https://servebolt.com/articles/profiling-sql-queries/)

Profiling performance involves analyzing a system or application’s behavior to identify bottlenecks, inefficiencies, and areas for optimization. This process typically involves collecting detailed information about resource usage, such as CPU and memory consumption, I/O operations, and execution time of functions or methods. Profiling tools can provide insights into how different parts of the code contribute to overall performance, highlighting slow or resource-intensive operations. By understanding these performance characteristics, developers can make targeted improvements, optimize code paths, and enhance system responsiveness and scalability. Profiling is essential for diagnosing performance issues and ensuring that applications meet desired performance standards.


#### [Back to top](#top)