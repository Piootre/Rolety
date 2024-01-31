# main.py
from mqtt_menage import MQTTManager
import http_config

def get_topic(topic):
    print('Topic: ',topic)
# Funkcja obsługi danych konfiguracyjnych MQTT
def mqtt_config_callback(topic, msg):
    # Tutaj można umieścić kod do obsługi otrzymanych danych MQTT w głównym programie
    print("Received message from topic {}: {}".format(topic, msg))

# Inicjalizacja managera MQTT
mqtt_manager = MQTTManager()

# Uruchamianie serwera HTTP
http_config.start_http_server(mqtt_manager)

# Subskrybuj temat MQTT
mqtt_manager.subscribe_to_topic(b"esp8266_data", mqtt_config_callback)

# Oczekiwanie w trybie czuwania
mqtt_manager.enter_idle_mode()
