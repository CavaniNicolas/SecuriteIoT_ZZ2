import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
	print("Connected with result code => "+mqtt.connack_string(rc))

def on_subscribe(client, userdata, mid, granted_qos):
	print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
	print("Received message '" + str(msg.payload) + "' on topic '" + msg.topic + "' with QoS" + str(msg.qos))
	if msg.retain == 1:
		print("This is a retained message")

def on_publish(client, userdata, mid):
	print("-- on_publish callback -- mid: " + str(mid) )

def Xor(inp, key):
	keyL = len(key)
	return [chr(ord(inp[i]) ^ ord(key[i % keyL])) for i in range(len(inp))]

def toCdecl(ch, prefix="char tab"):
	outp=list(ch)
	return prefix+"[{}]".format(len(outp)+1)+r"""="\x"""+(r"\x".join(["{:02x}".format(ord(_)) for _ in outp]))+r"""";"""


# client = mqtt.Client("GROUPE_CAVANI")
client = mqtt.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_connect = on_connect
client.on_publish = on_publish

try:
	# client.username_pw_set(username="SHANNON", password="PE300416EST")
	client.connect("172.16.32.8", 1883)

except:
	print("Connection Failed")

client.subscribe("/ISIMA/TP_5/#", qos=0)
client.loop_start()

while True:
	# (rc, mid) = client.publish(topic="/ISIMA/TP_5/GROUPE_12", payload="ON", qos=0)
	# print("Error return from publish of mid = " + str(mid) +" : " + mqtt.error_string(rc))
	time.sleep(5)

# defi 1
# "/ISIMA/SECRET_NGOKUCACILE/CHALLENGE_1/DEFI_2/GROUPE_CAVANI/LEDS/LED2"


#defi 2 
# "/ISIMA/SECRET_NGAKUWE/CHALLENGE_1/DEFI_2/GROUPE_CAVANI/LEDS/LED2"


#defi3 base:
# "/CTWYL/MGJNGS_EYLYKZE/IEEZAAXFA_1/HHZC_3/FNWRPG_OH/ZHBS/AAH2"
# decodéé: 
# /ISIMA/SECRET_AMAGAMA/CHALLENGE_1/DEFI_3/GROUPE_CAVANI/LEDS/LED2

#defi4 avec user et mdp
#/ISIMA/SECRET_ISIBONGO/CHALLENGE_1/DEFI_4/GROUPE_CAVANI/LEDS/LED2

#defi5 code Shannon
# /ISIMA/SECRET_UKUHLASELA/CHALLENGE_1/DEFI_5/GROUPE_CAVANI/LEDS/LED2

# X76T4H8M1V2
# 63K563K5
# X43XH3WHJ64
# PE300416EST
# CYNICISE
# ANTIQUAI
# SHANNON
# SARDINAI