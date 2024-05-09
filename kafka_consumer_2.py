from kafka import KafkaConsumer

# Configure Kafka
bootstrap_servers = 'localhost:29092'
# group_id = 'my-group'

# Define the topic to which you want to receive messages
topic = "demo-topic"

# Create a Kafka consumer
consumer = KafkaConsumer(topic,
                        #  group_id=group_id,
                         bootstrap_servers=bootstrap_servers)

# Define a function to handle messages
def consume_messages():
    print("waiting of messages...")
    for message in consumer:
        print(f"Received message: {message.value.decode('utf-8')}")

# Start consuming messages
consume_messages()
