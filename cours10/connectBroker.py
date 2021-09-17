import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code => "+mqtt.connack_string(rc))

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
    print("Received message '" + str(msg.payload) + "' on topic '" + msg.topic + "' with QoS " + str(msg.qos))

def on_publish(client, userdata, mid):
    print("--on_publish callback --mid: " + str(mid) )

client = mqtt.Client("G12GOOD")
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

client.on_connect = on_connect

try:
    client.username_pw_set(username="G12", password="isimaG12")

    # 8883: MQTT, chiffré
    # client.tls_set("keysNcertifs/mosquittoOrg/mosquitto.org.crt")
    # client.connect("test.mosquitto.org", 8883)

    # 8884: MQTT, chiffré, certificat client requis
    # client.tls_set("keysNcertifs/mosquittoOrg/mosquitto.org.crt", "keysNcertifs/mosquittoOrg/client.crt", "keysNcertifs/mosquittoOrg/client.key")
    # client.connect("test.mosquitto.org", 8884)

    # 8883: MQTT, chiffré. en local
    client.tls_set("keysNcertifs/mosquitto.org.crt")
    client.connect("localhost", 1883)

except:
    print("Connection Failed")

try:
    client.subscribe("/isima/G12", qos=0)
    client.loop_start()

    while True:
        (rc, mid) = client.publish(topic="/isima/G12", payload="TEST_G12 le BON message", qos=0)
        # (rc, mid) = client.publish(topic="isima/G13", payload="TEST_G13 test de base", qos=0)
        print("Error return from publish of mid = " + str(mid) +" : " + mqtt.error_string(rc))
        time.sleep(5)

except KeyboardInterrupt:
    client.loop_stop()
    client.unsubscribe("/isima/G12")
    client.disconnect()
    print("Done.")