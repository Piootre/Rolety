import network
import time
import machine
from umqtt.simple import MQTTClient

# Konfiguracja WiFi
wifi_ssid = "malina_2"
wifi_password = "bekon123"

# Konfiguracja MQTT
mqtt_broker = "broker.hivemq.com"
mqtt_port = 1883
mqtt_user = "Rolety"
mqtt_password = "Rolety123"
mqtt_topic = b"rolety/wybor"

#last_publish = time.time()
#publish_interval = 5

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(wifi_ssid, wifi_password)
        
        while not sta_if.isconnected():
            print("Attempting to connect....")
            time.sleep(1)
            
        print('Connected! Network config:', sta_if.ifconfig())
        
def sub_cb(topic, msg):
    print(topic, msg)
    
def reset():
    print("Resetting...")
    time.sleep(5)
    machine.reset()

def main():
    print(f"Begin connection with MQTT Broker :: {mqtt_broker}")
    mqttClient = MQTTClient('esp8266', mqtt_broker,mqtt_port, mqtt_user,mqtt_password, keepalive=60)
    mqttClient.set_callback(sub_cb)
    mqttClient.connect()
    mqttClient.subscribe(mqtt_topic)
    print(f"Connected to MQTT  Broker :: {mqtt_broker}, and waiting for callback function to be called!")
    while True:
            # Non-blocking wait for message
            mqttClient.check_msg()
            time.sleep(1)
            
if __name__ == "__main__":
    do_connect()
    while True:
        try:
            main()
        except OSError as e:
            print("Error: " +str(e))
            #reset()
