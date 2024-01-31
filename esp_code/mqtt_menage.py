# mqtt_manager.py
import time
from umqtt.simple import MQTTClient

class MQTTManager:
    def __init__(self):
        self.mqtt_client = None

    def connect_to_mqtt(self, server, port, username, password):
        client_id = "esp8266"
        self.mqtt_client = MQTTClient(client_id, server, port, username, password)
        self.mqtt_client.connect()

    def subscribe_to_topic(self, topic, callback):
        self.mqtt_client.set_callback(callback)
        self.mqtt_client.subscribe(topic)

    def check_messages(self):
        self.mqtt_client.check_msg()

    def disconnect_from_mqtt(self):
        self.mqtt_client.disconnect()

    def enter_idle_mode(self):
        while True:
            time.sleep(1)
            # Tutaj możesz umieścić inne operacje w stanie czuwania
