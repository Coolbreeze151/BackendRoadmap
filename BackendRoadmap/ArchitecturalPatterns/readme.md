### [Back Home](../../README.md)

# Architectural Patterns

## Table of Contents

- [Monolithic Apps](#monolithic-apps)
- [Microservices](#microservices)
- [SOA](#soa)
- [Serverless](#serverless)
- [Service Mesh](#service-mesh)
- [Twelve Factor Apps](#twelve-factor-apps)

## [Monolithic Apps](https://microservices.io/patterns/monolithic.html)

Monolithic applications are designed as a single, cohesive unit. All components of the application are interconnected and interdependent. This architecture is straightforward to develop and deploy but can become difficult to manage and scale as the application grows.

## [Microservices](https://microservices.io/patterns/microservices.html)

Microservices architecture breaks down an application into smaller, independent services that communicate over a network. Each service is responsible for a specific functionality and can be developed, deployed, and scaled independently. This approach offers greater flexibility and scalability but introduces complexity in terms of service coordination and communication.

## [SOA](https://aws.amazon.com/what-is/service-oriented-architecture/)

Service-Oriented Architecture (SOA) is a design pattern where services are provided to other components by application components, through a communication protocol over a network. SOA allows for integration of various services, promoting reusability and interoperability. It is similar to microservices but typically involves larger, more complex services.

## [Serverless](https://www.ibm.com/topics/serverless)

Serverless architecture allows developers to build and run applications without managing the underlying infrastructure. Cloud providers automatically allocate resources as needed, and users are billed based on their actual usage. This model simplifies deployment and scaling but can lead to vendor lock-in and may not be suitable for all types of applications.

## [Service Mesh](https://aws.amazon.com/what-is/service-mesh/)

A service mesh is a dedicated infrastructure layer for handling service-to-service communication. It provides features like load balancing, service discovery, and security, abstracting these concerns away from the application code. Service meshes are particularly useful in microservices architectures to manage the complexity of inter-service communication.

## [Twelve Factor Apps](https://12factor.net/)

The Twelve-Factor App methodology is a set of best practices for building modern, scalable, and maintainable web applications. It covers aspects such as codebase management, dependencies, configuration, backing services, build and release processes, and more. Adhering to these principles helps ensure that applications are portable, resilient, and easy to deploy.

### [Back to top](#top)
