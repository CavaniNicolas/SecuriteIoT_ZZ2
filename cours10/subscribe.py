import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	print("Connected with result code => "+mqtt.connack_string(rc))

def on_subscribe(client, userdata, mid, granted_qos):
	print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
	print("Received message '" + str(msg.payload) + "' on topic '" + msg.topic + "' with QoS" + str(msg.qos))

client = mqtt.Client("G12")
client.on_subscribe = on_subscribe
client.on_message = on_message
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
	client.tls_set("keysNcertifs/local/serveur.crt")
	client.connect("localhost", 1883)

except:
	print("Connection Failed")

try:
	client.subscribe("/isima/#", qos=0)
	client.loop_forever()

except KeyboardInterrupt:
    client.loop_stop()
    client.unsubscribe("#")
    client.disconnect()
    print("Done.")