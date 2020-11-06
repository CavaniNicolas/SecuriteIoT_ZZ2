
import random
import base64

def Xor(inp, key):
	keyL = len(key)
	return [chr(ord(inp[i]) ^ ord(key[i % keyL])) for i in range(len(inp))]

def toCdecl(ch, prefix="char tab"):
	outp=list(ch)
	return prefix+"[{}]".format(len(outp)+1)+r"""="\x"""+(r"\x".join(["{:02x}".format(ord(_)) for _ in outp]))+r"""";"""

def toCdecl2(ch):
	outp=list(ch)
	return r"\x"+(r"\x".join(["{:02x}".format(ord(_)) for _ in outp]))+r""

# if __name__ == '__main__':
# 	key = "CLEF"
# 	for i in range (16):
# 		if (random.randint(0, 1) == 1):
# 			payload = "ON"
# 		else:
# 			payload = "OFF"
# 		payload = payload + "{}".format(i+1)
# 		# print (toCdecl2(Xor(payload, key)))
# 		print (payload)

def hexStringToBinary(mystr):
	# Code to convert hex initial string to binary 
	res = bin(int(mystr, 16)).zfill(8) 
	# Return the resultant string
	return res # return str(res) fait la meme chose though

hexstr = toCdecl2(Xor("ON", "CLEF"))
print (hexstr)
for i in range (0, len(hexstr), 4):
	hex1str = hexstr[i+2:i+4]
	print(type(hex1str))
	print(hex1str)
	# print (int("0x1a", 16))
	# print (int("\x1a", 16))
	print (int(hex1str, 16))

	print(str(hexStringToBinary(hex1str)))
	print(hexStringToBinary(hex1str))
	print(type(hexStringToBinary(hex1str)))

# print (base64.standard_b64encode(0b12))