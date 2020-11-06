import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	print("Connected with result code => "+mqtt.connack_string(rc))

def on_subscribe(client, userdata, mid, granted_qos):
	print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
	print("Received message '" + str(msg.payload) + "' on topic '" + msg.topic + "' with QoS" + str(msg.qos))

client = mqtt.Client("G122")
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_connect = on_connect

try:
	client.username_pw_set(username="G122", password="isimaG122")
	client.connect("127.0.0.1", 1883)
except:
	print("Connection Failed")

try:
	client.subscribe("/isima/G12/#", qos=0)
	client.loop_forever()

except KeyboardInterrupt:
    client.loop_stop()
    client.unsubscribe("/isima/G12/#")
    client.disconnect()
    print("Done.")