from confluent_kafka import Consumer, KafkaException

# Kafka consumer configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'
}

# Initialize the consumer
consumer = Consumer(**conf)
consumer.subscribe(['my_topic'])

# Poll messages from Kafka topic
try:
    while True:
        msg = consumer.poll(1.0)  # Poll timeout set to 1 second
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                print(f"{msg.topic()} [{msg.partition()}] reached end at offset {msg.offset()}")
            else:
                raise KafkaException(msg.error())
        else:
            # Successfully received message
            print(f"Received message: {msg.value().decode('utf-8')}")

except KeyboardInterrupt:
    pass
finally:
    # Close down the consumer
    consumer.close()
