from kafka import KafkaProducer
from db_crud import fetch_all_user
import time
import json
from format_file import wrap_String_In_HTMLMac, original_format

producer_form_db = KafkaProducer(bootstrap_servers=["localhost:9092"])
if __name__ == "__main__":
    while True:
        for item in fetch_all_user("kafka_users"):
            for key, value in item.items():
                if key == "createdAt" and value > '2000':
                    print("User young = ", item)
                    producer_form_db.send('recieved_user_db_topic',
                                          json.dumps(item, default=str).encode('utf-8'),
                                          partition=0)
                elif key == "createdAt" and value < '2000':
                    print("User old = ", item)
                    producer_form_db.send('recieved_user_db_topic',
                                          json.dumps(item, default=str).encode('utf-8'),
                                          partition=1)
        time.sleep(10)
        wrap_String_In_HTMLMac("index.html", original_format())
