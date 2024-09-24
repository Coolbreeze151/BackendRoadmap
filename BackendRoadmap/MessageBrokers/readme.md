### [Back Home](../../README.md)

# Message Brokers

## Table of Contents

   - [What is a Message Broker](#what-is-a-message-broker)
   - [What is Kafka?](#what-is-kafka)
   - [Key Components of Kafka](#key-components-of-kafka)
   - [How Kafka Works](#how-kafka-works)
   - [Kafka Architecture Overview](#kafka-architecture-overview)
   - [Pros and Cons of Kafka](#pros-and-cons-of-kafka)
     - [Pros](#pros)
     - [Cons](#cons)
   - [Installation and Setup](#installation-and-setup)
   - [Python Kafka Scripts](#python-kafka-scripts)
   - [Conclusion](#conclusion)

## What is a Message Broker
Message brokers are intermediaries that facilitate communication between distributed systems or components by receiving, routing, and delivering messages. They enable asynchronous message passing, decoupling producers (senders) from consumers (receivers), which improves scalability and flexibility. Common functions of message brokers include message queuing, load balancing, and ensuring reliable message delivery through features like persistence and acknowledgment. Popular message brokers include Apache Kafka, RabbitMQ, and ActiveMQ, each offering different features and capabilities suited to various use cases like real-time data processing, event streaming, or task management. More information on message brokers can be found [here](https://www.ibm.com/topics/message-brokers).


## What is Kafka?
Apache Kafka is a distributed event streaming platform designed to handle large-scale, real-time data feeds with high throughput, low latency, and fault tolerance. It was originally developed by LinkedIn and open-sourced through the Apache Software Foundation. Kafka enables applications to publish, subscribe, store, and process streams of records in a distributed, durable, and fault-tolerant way.

Kafka is widely used in various applications such as messaging systems, log aggregation, event sourcing, and stream processing. It can handle high volumes of real-time data and seamlessly integrates with many systems like Hadoop, Spark, and Flink.

## Key Components of Kafka
1. Producer: Sends messages to a Kafka topic.

2. Consumer: Reads messages from a Kafka topic.

3. Broker: A Kafka cluster is made up of multiple brokers, which handle the receiving, storing, and serving of records.

4. Topic: A named stream of records to which producers send data and from which consumers read.

5. Partition: Kafka topics are divided into partitions for scalability and fault tolerance.

6. Zookeeper: Used to coordinate brokers in a Kafka cluster (in older versions of Kafka). Starting from version 2.8, Kafka introduced the removal of Zookeeper dependency

## How Kafka Works
Kafka follows a publish-subscribe model where:

- Producers send messages (events) to Kafka topics.

- Messages in topics are split into partitions and are replicated across Kafka brokers to ensure fault tolerance.

- Consumers subscribe to topics and process the messages asynchronously.

## Kafka Architecture Overview
Kafka architecture is highly distributed and scalable. Kafka brokers form a cluster, which can handle failovers and load balancing. Kafka provides the capability to handle large amounts of messages by distributing data across different brokers and partitions, providing horizontal scalability.

Kafka also has a replication feature that ensures fault tolerance by storing replicas of partitions across different brokers.

## Pros and Cons of Kafka
### Pros:
1. High Throughput: Kafka can handle millions of messages per second, making it ideal for high-volume data streaming.

2. Scalability: Kafka’s architecture is distributed and allows horizontal scaling by adding more brokers.

3. Durability: Kafka stores messages on disk and replicates them across brokers, ensuring data persistence and reliability.

4. Fault Tolerance: Kafka replicates partitions across brokers, enabling it to continue operating even if some brokers fail.

5. Real-time Processing: Kafka’s low latency and high throughput make it ideal for real-time applications like log aggregation, monitoring, and event-driven systems.

6. Distributed Architecture: Kafka’s distributed nature makes it robust against failures and capable of handling large-scale data.

7. Integration: Kafka integrates easily with stream processing frameworks (e.g., Kafka Streams, Apache Flink, Apache Spark).

### Cons:
1. Complexity: Setting up and managing a Kafka cluster can be complex, especially for beginners.

2. Operational Overhead: Managing Kafka brokers, Zookeeper, partitions, and replicas can require significant operational overhead.

3. Ordering Guarantees: Kafka provides ordering guarantees within a partition but not across partitions, which can be tricky for certain use cases.

4. Message Delivery Semantics: Kafka supports at least once and exactly once semantics but may require extra configuration to ensure the desired level of message delivery reliability.

5. Latency for Small Messages: While Kafka is optimized for high throughput, it can introduce noticeable latency when dealing with small messages or low traffic.

## Installation and Setup
Before using Kafka, ensure that you have installed Apache Kafka and have it running on your local machine or server. You can find the official installation guide [here](https://kafka.apache.org/quickstart).

## Python Kafka Scripts
Within this folder are some example scripts to get you started with Kafka in Python using the confluent-kafka library.

- Producer Script: Demonstrates sending JSON data to a Kafka topic.
- Consumer Script: Shows how to read messages from a Kafka topic.
- Auto-Commit Disabled Consumer: Useful when fine control over offset committing is required.


## Conclusion
Kafka is an incredibly powerful tool for distributed streaming and real-time data processing. It shines in scenarios that require handling high-throughput, low-latency, and fault-tolerant data streams. However, it requires careful management and is best suited for large-scale or real-time use cases where those capabilities are critical.

For further learning, refer to Kafka’s [official documentation](https://kafka.apache.org/documentation/) and the [Kafka Python client documentation](https://docs.confluent.io/kafka-clients/python/current/overview.html).


[Back to top](#top)



