from kafka import KafkaConsumer

print("Starting consumer...")

consumer = KafkaConsumer(
    "user-events",
    bootstrap_servers="localhost:9094",
    auto_offset_reset="earliest",
    consumer_timeout_ms=10000
)

print("Reading messages...")

for message in consumer:
    print(message.value.decode("utf-8"))

print("Done reading.")