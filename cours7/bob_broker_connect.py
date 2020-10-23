import paho.mqtt.client as mqtt
import time

from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PublicKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

# Topics List
topic_public_key = "/ISIMA/TP_7/GROUPE_12/public_key"
topic_messages = "/ISIMA/TP_7/GROUPE_12/messages"

# Generate private and public keys for use in the exchange.
Alice_private_key = X25519PrivateKey.generate()
Alice_public_key = Alice_private_key.public_key()

# Pour pouvoir envoyer la clef dans le payload
A_public_key  = Alice_public_key.public_bytes(encoding=serialization.Encoding.Raw, format=serialization.PublicFormat.Raw) # type = bytes
# A_public_key_clean = A_public_key.decode('utf-8')

Bob_public_key = b"0" # type = bytes

shared_Key = b"0" # type = bytes

def on_connect(client, userdata, flags, rc):
	print("Connected with result code => "+mqtt.connack_string(rc))

def on_subscribe(client, userdata, mid, granted_qos):
	print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message_public_key(msg):
	global Bob_public_key
	global shared_Key
	# Si on ne recoie pas notre propre publication, on envoie la notre en retour
	# ET Si on ne la pas deja recu, on la stock
	if (A_public_key != msg.payload and Bob_public_key == b"0"):
		# On stocke la clef publique recue
		Bob_public_key = msg.payload
		# On calcul la clef partagee
		shared_Key = getSharedKey(Bob_public_key)
		print(shared_Key)

		# On publie la notre
		(rc, mid) = client.publish(topic=topic_public_key, payload=A_public_key, qos=0)
		print("Error return from publish of mid = " + str(mid) +" : " + mqtt.error_string(rc))


def on_message(client, userdata, msg):

	# Si le message recu est peut etre la clef publique de Bob
	if (msg.topic == topic_public_key):
		on_message_public_key(msg)

	# Sinon c'est un message classique
	else:
		print("Received message '" + str(msg.payload) + "' on topic '" + msg.topic + "' with QoS" + str(msg.qos))

	if msg.retain == 1:
		print("This is a retained message")

def on_publish(client, userdata, mid):
	print("-- on_publish callback -- mid: " + str(mid) )

# def Xor(inp, key):
# 	keyL = len(key)
# 	return [chr(ord(inp[i]) ^ ord(key[i % keyL])) for i in range(len(inp))]

# def toCdecl(ch, prefix="char tab"):
# 	outp=list(ch)
# 	return prefix+"[{}]".format(len(outp)+1)+r"""="\x"""+(r"\x".join(["{:02x}".format(ord(_)) for _ in outp]))+r"""";"""

# def stringToHex(myStr):
# 	myHex = myStr.encode('utf-8').hex()
# 	# print(myHex)
# 	return myHex.upper()

# def hexToString(myHex):
# 	bytes_object = bytearray.fromhex(myHex) #Convert to bytes object
# 	ascii_string = bytes_object.decode('ASCII') #Convert to ASCII representation
# 	# print(ascii_string)
# 	return ascii_string

def getSharedKey(peer_public_key):
	shared_Key = Alice_private_key.exchange(X25519PublicKey.from_public_bytes(peer_public_key))
	return shared_Key

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

client.subscribe(topic_public_key, qos=0)
client.subscribe(topic_messages, qos=0)
client.loop_start()

print(A_public_key)

while True:
	# Si on a pas la clef publique de Bob, on publie la notre dans l'espoir que Bob reponde avec la sienne
	if (Bob_public_key == b"0"):
		# On publie notre clef publique
		(rc, mid) = client.publish(topic=topic_public_key, payload=A_public_key, qos=0)
		print("Error return from publish of mid = " + str(mid) +" : " + mqtt.error_string(rc))

	# (rc, mid) = client.publish(topic="/ISIMA/TP_7/GROUPE_12/Bob_messages", payload="ON", qos=0)
	# print("Error return from publish of mid = " + str(mid) +" : " + mqtt.error_string(rc))
	time.sleep(5)
