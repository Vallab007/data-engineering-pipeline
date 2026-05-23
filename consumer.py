from kafka import KafkaConsumer
import json
import psycopg2

print("Starting consumer...")
print("Reading messages...")

# PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",
    database="events_db",
    user="airflow",
    password="airflow",
    port=5432
)

cursor = conn.cursor()

consumer = KafkaConsumer(
    'user-events',
    bootstrap_servers='localhost:9094',
    auto_offset_reset='earliest',
    group_id='postgres-group-1',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    data = message.value

    print(data)

    cursor.execute(
        """
        INSERT INTO events (user_id, event, event_time)
        VALUES (%s, %s, %s)
        """,
        (
            data['user_id'],
            data['event'],
            data['timestamp']
        )
    )

    conn.commit()