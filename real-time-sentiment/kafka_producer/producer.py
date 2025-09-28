import json
import time
import random
from kafka import KafkaProducer

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

BROKER = config["kafka_broker"]
TOPIC = config["topic"]

# Create Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=[BROKER],
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Mock messages
sample_tweets = [
    "I love using this app, it's so smooth!",
    "Worst experience ever, not recommended.",
    "Feeling neutral about the update...",
    "This product is amazing and works well!",
    "Terrible performance and lots of bugs!",
    "Decent but could use some improvements."
]

print(f"✅ Sending messages to topic: {TOPIC}")

try:
    while True:
        message = {
            "user": f"user_{random.randint(1, 1000)}",
            "text": random.choice(sample_tweets),
            "timestamp": time.time()
        }
        producer.send(TOPIC, value=message)
        print(f"Sent -> {message}")
        time.sleep(2)  # simulate stream delay
except KeyboardInterrupt:
    print("❌ Producer stopped manually.")
finally:
    producer.flush()
    producer.close()
