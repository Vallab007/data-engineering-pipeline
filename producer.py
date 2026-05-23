from kafka import KafkaProducer
import json
import time
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers="localhost:9094",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

events = ["login", "view_product", "add_to_cart", "purchase", "logout"]

for i in range(10):
    message = {
        "user_id": 100 + i,
        "event": events[i % len(events)],
        "timestamp": datetime.now().isoformat()
    }

    producer.send("user-events", message)
    print("Sent:", message)
    time.sleep(2)

producer.flush()
producer.close()