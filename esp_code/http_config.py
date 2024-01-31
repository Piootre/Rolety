# http_config.py
import network
import usocket as socket
from mqtt_menage import MQTTManager
#from main import get_topic

def start_http_server(mqtt_menage):
    # Inicjalizacja punktu dostępowego
    ap_ssid = "ESP8266-AP"
    ap_password = "haslo1234"
    ap_wifi = network.WLAN(network.AP_IF)
    ap_wifi.active(True)
    ap_wifi.config(essid=ap_ssid, password=ap_password, authmode=network.AUTH_WPA_WPA2_PSK)

    print(ap_wifi.ifconfig())

    # Strona konfiguracyjna
    html = """<!DOCTYPE html>
    <html>
    <head><title>Konfiguracja ESP8266</title></head>
    <body>
        <h1>Konfiguracja ESP8266</h1>
        <form action="/save_config" method="post">
            <label for="ssid">SSID:</label>
            <input type="text" name="ssid" required><br>

            <label for="password">Hasło WiFi:</label>
            <input type="password" name="password" required><br>

            <label for="mqtt_server">Serwer MQTT:</label>
            <input type="text" name="mqtt_server" required><br>

            <label for="mqtt_port">Port MQTT:</label>
            <input type="text" name="mqtt_port" required><br>

            <label for="mqtt_username">Użytkownik MQTT:</label>
            <input type="text" name="mqtt_username" required><br>

            <label for="mqtt_password">Hasło MQTT:</label>
            <input type="password" name="mqtt_password" required><br>

            <input type="submit" value="Zapisz konfigurację">
        </form>
    </body>
    </html>
    """

    def connect_to_wifi(ssid, password):
        sta_wifi = network.WLAN(network.STA_IF)
        sta_wifi.active(True)
        sta_wifi.connect(ssid, password)

    # Gniazdo do obsługi żądań HTTP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.4.1', 80))  # Adres IP punktu dostępowego i port 80
    server_socket.listen(1)

    print("Oczekiwanie na połączenie...")

    while True:
        conn, addr = server_socket.accept()
        print('Połączono z', addr)

        request = conn.recv(1024).decode('utf-8')
        print('Otrzymane żądanie:\n', request)

        if request.startswith("POST /save_config"):
            # Odczytaj dane z formularza
            content_length_start = request.find("Content-Length:")
            content_length_end = request.find("\r\n", content_length_start)
            content_length = int(request[content_length_start + 15:content_length_end].strip())

            form_data = conn.recv(content_length).decode('utf-8')

            # Odczytaj dane z formularza
            ssid_start = form_data.find("ssid=") + 5
            ssid_end = form_data.find("&", ssid_start)
            ssid = form_data[ssid_start:ssid_end]

            password_start = form_data.find("password=") + 9
            password_end = form_data.find("&", password_start)
            password = form_data[password_start:password_end]

            mqtt_server_start = form_data.find("mqtt_server=") + 12
            mqtt_server_end = form_data.find("&", mqtt_server_start)
            mqtt_server = form_data[mqtt_server_start:mqtt_server_end]

            mqtt_port_start = form_data.find("mqtt_port=") + 10
            mqtt_port_end = form_data.find("&", mqtt_port_start)
            mqtt_port = form_data[mqtt_port_start:mqtt_port_end]

            mqtt_username_start = form_data.find("mqtt_username=") + 14
            mqtt_username_end = form_data.find("&", mqtt_username_start)
            mqtt_username = form_data[mqtt_username_start:mqtt_username_end]

            mqtt_password_start = form_data.find("mqtt_password=") + 14
            mqtt_password_end = form_data.find("&", mqtt_password_start)
            mqtt_password = form_data[mqtt_password_start:mqtt_password_end]
            
            mqtt_topic_start = form_data.find("mqtt_password=") + 14
            mqtt_topic_end = form_data.find("&", mqtt_topic_start)
            mqtt_topic = form_data[mqtt_topic_start:mqtt_topic_end]

            # Zapisz konfigurację
            print("SSID:", ssid)
            print("Hasło WiFi:", password)
            print("Serwer MQTT:", mqtt_server)
            print("Port MQTT:", mqtt_port)
            print("Użytkownik MQTT:", mqtt_username)
            print("Hasło MQTT:", mqtt_password)
            print("Topic:",mqtt_topic)

            # Połącz się z WiFi
            connect_to_wifi(ssid, password)

            # Przekaż dane do serwera MQTT
            mqtt_menager.connect_to_mqtt(mqtt_server, int(mqtt_port), mqtt_username, mqtt_password,topic)
            #get_topic(mqtt_topic)
            # Odpowiedz klientowi
            response = "HTTP/1.1 302 Found\r\nLocation: /\r\n\r\n"
            conn.send(response.encode('utf-8'))
        else:
            # Odpowiedz strona konfiguracyjną
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + html
            conn.send(response.encode('utf-8'))

        conn.close()

if __name__ == "__main__":
    mqtt_menager = MQTTManager()
    start_http_server(mqtt_config_callback)

