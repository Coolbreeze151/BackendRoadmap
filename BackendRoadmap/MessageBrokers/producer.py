from confluent_kafka import Producer
import json

# Kafka producer configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}

# Initialize the producer
producer = Producer(**conf)

# Delivery report callback
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Produce a message
message_value = {'key': 'value', 'example': 'data'}
producer.produce(
    'my_topic',
    key='my_key',
    value=json.dumps(message_value),
    callback=delivery_report
)

# Wait for all messages to be delivered
producer.flush()
