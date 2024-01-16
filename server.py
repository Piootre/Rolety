import ssl
from paho import mqtt
import paho.mqtt.client as paho
import paho.mqtt.publish as publish

def send_message(topic, msg,):
    
    msgs = {'topic': topic, 'payload': msg}

    # use TLS for secure connection with HiveMQ Cloud
    sslSettings = ssl.SSLContext(mqtt.client.ssl.PROTOCOL_TLS)

    # put in your cluster credentials and hostname
    auth = {'username': "Rolety", 'password': "Rolety123"}

    publish.multiple(msgs, hostname="bae7e674a7ff46e0a54ac9fe9afe407d.s1.eu.hivemq.cloud", port=8883, auth=auth,
                    tls=sslSettings, protocol=paho.MQTTv31)
    
send_message("rolety/wybor", "r1")