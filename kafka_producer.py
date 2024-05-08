from kafka import KafkaProducer
import time

# Configure Kafka
bootstrap_servers = 'localhost:29092'

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Define the topic to which you want to send messages
topic = "demo-topic"

# Define a function to send messages
def send_message(msg):
    producer.send(topic, msg.encode('utf-8'))
    print(f"Sent: {msg}")

# Send some messages
for i in range(5):
    send_message(f"Message {i}")
    time.sleep(1)

# Close the producer
producer.close()