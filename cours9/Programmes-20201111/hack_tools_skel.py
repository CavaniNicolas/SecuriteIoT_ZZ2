import paho.mqtt.client as mqtt
import time

IP = "172.16.32.7"
PORT = 10801
GROUPE = "GROUPE_XX"
SECRET = "........"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code => "+mqtt.connack_string(rc))
    client.connected=(rc==0)

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: mid: " + str(mid) + " QoS" + str(granted_qos))

def on_message(client, userdata, msg):
    print("Received message '" + str(msg.payload) + "' on topic '" + msg.topic + "' with QoS " + str(msg.qos))
    if "LED2_HACKED" in msg.topic and GROUPE in msg.topic:
        client.hacked=True
        print("\nWell done !")

    #Construction du nouveau payload ICI

    if False:#si construction payload OK :
        topic=msg.topic
        topic=topic.replace("GROUPE_XX",GROUPE)
        topic=topic.replace("LED1","LED2")
        client.publish(topic,newpayload)

def on_publish(client, userdata, mid):
    print("--on_publish callback --mid: " + str(mid) )

client = mqtt.Client(GROUPE)
client.connected=False
client.hacked=False
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

try:
    #client.username_pw_set(username="ANTIMUON", password="BY876F7F")
    client.connect(IP, PORT)
    client.subscribe("#", qos=0)
    client.loop_start()

    while not client.hacked:
        time.sleep(5)
        if client.connected:
            (rc, mid) = client.publish(topic="/ISIMA/SECRET_{}/CHALLENGE_1/DEFI_1/{}/LEDS/LED2".format(SECRET,GROUPE), payload="ON", qos=0)
            print("Return from publish of mid = " + str(mid) +" : " + mqtt.error_string(rc))
        else:
            break

except ConnectionRefusedError:
    print("Connection Failed Bad IP / PORT")

except KeyboardInterrupt:
    pass

print("Break signal")
client.loop_stop()
client.unsubscribe("#")
client.disconnect()
print("Done.")



