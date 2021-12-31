from kafka import KafkaProducer
from data import get_registered_user
import time
import json


producer = KafkaProducer(bootstrap_servers=["localhost:9092"])
if __name__ == "__main__":
    while 1 == 1:
        register_user = get_registered_user()
        print(register_user)
        producer.send('generated_user_topic', json.dumps(register_user).encode('utf-8'))
        time.sleep(4)
