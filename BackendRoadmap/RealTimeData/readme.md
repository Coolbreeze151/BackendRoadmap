### [Back Home](../../README.md)

# Real Time Data

## Table of Contents

- [Introduction to Real-Time Data](#introduction-to-real-time-data)
- [Server-Sent Events (SSE)](#1-server-sent-events-sse)
    - [What are Server-Sent Events?](#what-are-server-sent-events)
    - [Key Characteristics](#key-characteristics)
    - [Example Use Case](#example-use-case)
    - [Pros](#pros)
    - [Cons](#cons)
    - [Example Code](#example-code)
 - [WebSockets](#2-websockets)
    - [What are WebSockets?](#what-are-websockets)
    - [Key Characteristics](#key-characteristics-1)
    - [Example Use Case](#example-use-case-1)
    - [Pros](#pros-1)
    - [Cons](#cons-1)
    - [Example Code](#example-code-1)
- [Long Polling](#3-long-polling)
    - [What is Long Polling?](#what-is-long-polling)
    - [Key Characteristics](#key-characteristics-2)
    - [Example Use Case](#example-use-case-2)
    - [Pros](#pros-2)
    - [Cons](#cons-2)
    - [Example Code](#example-code-2)
- [Short Polling](#4-short-polling)
    - [What is Short Polling?](#what-is-short-polling)
    - [Key Characteristics](#key-characteristics-3)
    - [Example Use Case](#example-use-case-3)
    - [Pros](#pros-3)
    - [Cons](#cons-3)
    - [Example Code](#example-code-3)

## Introduction to Real-Time Data
Real-time data refers to the continuous and immediate transmission of information from a server to a client or between systems. In modern web applications, real-time data exchange is crucial for functionalities like live updates, notifications, chat systems, gaming, stock tickers, IoT, and more.

Various techniques and protocols enable real-time communication between a client (e.g., a web browser or mobile app) and a server. Below are some of the most commonly used techniques for enabling real-time data transmission:

## 1. Server-Sent Events (SSE)
### What are Server-Sent Events?
Server-Sent Events (SSE) is a server-to-client communication protocol allowing servers to push real-time updates to the client over a single, long-lived HTTP connection. With SSE, a client (browser) makes a request to the server, and the server streams updates back to the client as events occur.

### Key Characteristics:
- Unidirectional: Data is only pushed from the server to the client.

- Utilizes a persistent HTTP connection.

- Supported natively by modern browsers via the EventSource API.

- Ideal for scenarios like live news feeds, notifications, or real-time analytics.

### Example Use Case:
SSE is ideal for situations where you want continuous, real-time updates from the server to the client, such as:

- Real-time stock market updates
- Live sports scores
- Breaking news alerts

### Pros:
- Simple to implement.
- Lightweight compared to WebSockets.
- Automatically reconnects when the connection is lost.

### Cons:
- Unidirectional: The client cannot send messages to the server over the same connection.
- Not supported by all browsers (e.g., Internet Explorer).
- Limited to HTTP/1.1 and suffers from connection limitations in environments with large-scale clients.

### Example Code
```javascript
const eventSource = new EventSource('/events');
eventSource.onmessage = function(event) {
    console.log('New event:', event.data);
};
```


## 2. WebSockets
### What are WebSockets?
WebSockets provide a full-duplex communication channel over a single, long-lived TCP connection. Unlike traditional HTTP, WebSockets allow both the client and server to send data to each other at any time, making them a great choice for interactive, real-time applications.

### Key Characteristics:
- Bidirectional: Both client and server can send data at any time.
- Operates over TCP using a WebSocket handshake.
- Ideal for applications requiring low-latency, real-time bidirectional communication.

### Example Use Case:
WebSockets are commonly used for:

- Real-time chat applications.
- Online gaming.
- Collaborative platforms (e.g., Google Docs real-time editing).
- Live-streaming and broadcasting.

### Pros:
- Efficient and low-latency communication.
- Persistent connection reduces overhead from HTTP request/response cycles.
- Suitable for highly interactive applications.

### Cons:
- More complex to set up compared to HTTP-based solutions.
- Requires server support for WebSocket protocol.
- Connection and reconnection management can be tricky.

### Example Code
#### Client Side Javascript
```javascript
const socket = new WebSocket('ws://example.com/socket');

// Send a message
socket.onopen = function() {
    socket.send('Hello Server!');
};

// Receive a message
socket.onmessage = function(event) {
    console.log('Received from server:', event.data);
};
```
#### Server Side Nodejs
```javascript
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', (ws) => {
    ws.on('message', (message) => {
        console.log('Received:', message);
        ws.send('Hello from the server!');
    });
});
```

## 3. Long Polling
### What is Long Polling?
Long polling is a technique where the client repeatedly makes HTTP requests to the server, but the server holds the request open until new data becomes available. Once new data is available, the server responds to the request, and the client immediately makes another request, effectively creating a loop.

### Key Characteristics:
- Simulates real-time communication over HTTP.
- Client continuously waits for updates from the server.
-  Keeps the HTTP connection open until a response is ready.

### Example Use Case:
Long polling is useful for:

- Web applications that need to simulate real-time behavior but don't need continuous streaming.
- Environments where WebSockets are not available or supported.

### Pros:
- Works with existing HTTP/1.1 infrastructure.
- Easier to implement with firewalls and proxies compared to WebSockets.

### Cons:
- Higher latency compared to WebSockets and SSE.
- More resource-intensive due to repeated HTTP requests.
- Not true real-time communication, as there can be delays between requests.

### Example Code:
```javascript
function longPoll() {
    fetch('/poll-endpoint')
        .then(response => response.json())
        .then(data => {
            console.log('Received data:', data);
            longPoll(); // Start a new poll
        })
        .catch(error => {
            console.error('Error:', error);
            setTimeout(longPoll, 5000); // Retry after 5 seconds
        });
}

longPoll();
```

## 4. Short Polling
### What is Short Polling?
Short polling is a less efficient polling technique where the client regularly makes HTTP requests to the server at fixed intervals (e.g., every few seconds) to check for new data. Unlike long polling, the server does not hold the connection open and responds immediately, even if there is no new data available.

### Key Characteristics:
- Fixed interval HTTP requests.
- Simpler than long polling but introduces latency.
- Inefficient in terms of network resources.

### Example Use Case:
Short polling is suitable for:

- Applications where data freshness is not critical.
- Low-frequency update systems such as background synchronization.

### Pros:
- Easy to implement with standard HTTP requests.
- No need for persistent connections or special protocols.

### Cons:

- Higher server load due to frequent polling.
- Not efficient for real-time applications.
- Latency between updates as the client waits for the next polling interval.

### Example Code:
```javascript
function shortPoll() {
    setInterval(() => {
        fetch('/poll-endpoint')
            .then(response => response.json())
            .then(data => {
                console.log('Received data:', data);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }, 5000); // Poll every 5 seconds
}

shortPoll();
```

[Back to Top](#top)