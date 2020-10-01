import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	print("Connected with result code => " + mqtt.connack_string(rc))

client = mqtt.Client()
client.on_connect = on_connect

try:
	client.username_pw_set(username="G12", password="isimaG12")
	client.connect("hairdresser-01.cloudmqtt.com", 18972)

except:
	print("Connection Failed")

client.loop_forever()
