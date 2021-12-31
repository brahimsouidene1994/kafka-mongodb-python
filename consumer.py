from kafka import KafkaConsumer
import json
from db_crud import insert_new_user

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "generated_user_topic",
        bootstrap_servers=["localhost:9092"],
        auto_offset_reset="earliest",
        group_id="group_consumer_A"
    )

    print("consumer is reading data :")
    for msg in consumer:
        print("User new = ", json.loads(msg.value))
        insert_new_user(json.loads(msg.value), "kafka_users")
