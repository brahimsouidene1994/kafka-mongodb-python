from kafka import KafkaConsumer
import json
from format_file import append_new_tag_file, wrap_String_In_HTMLMac, render_file, original_format
import pyautogui


if __name__ == "__main__":
    consumer_db = KafkaConsumer(
        "recieved_user_db_topic",
        bootstrap_servers=["localhost:9092"],
        auto_offset_reset="earliest",
        group_id="group_consumer_A"
    )

    wrap_String_In_HTMLMac("index.html", original_format())
    print("reading data :")
    render_file("index.html")
    for msg in consumer_db:
        if msg.partition == 0:
            wrap_String_In_HTMLMac("index.html", str(append_new_tag_file(json.loads(msg.value), "users-two")))
        elif msg.partition == 1:
            wrap_String_In_HTMLMac("index.html", str(append_new_tag_file(json.loads(msg.value), "users-one")))
        pyautogui.hotkey('f5')  # Simulates F5 key press = page refresh
