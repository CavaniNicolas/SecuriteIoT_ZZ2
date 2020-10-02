
# "Man python"
# >>> dir(bytes)
# >>> help(bytes.decode)

ifilename = "ch1_defi4_2020.hex"
ofilename = "myHexDefi4.txt"


def stringToHex(myStr):

	# for character in myStr:
	# 	print(character)
	# 	print(character, character.encode('utf-8').hex())

	myHex = myStr.encode('utf-8').hex()
	# print(myHex)
	return myHex.upper()

# print(stringToHex("Bonjour"))
# stringToHex("BONJOUR")

# NE FONCTIONNE PAS BIEN (avec les fichiers)
# myHex must not contain '0x' at the begining
def hexToStringBytes(myHex):
	# print(myHex)

	bytes_object = bytearray.fromhex(myHex) #Convert to bytes object
	ascii_string = ""
	for i in bytes_object:
		b = (i).to_bytes(2, byteorder='big')
		try:
			c = b.decode("ascii")
			# print("      c: ", c)
		except:
			c = "?"
		ascii_string += c
	# print(ascii_string)
	return ascii_string

# FONCTIONNE
def hexToStringBytes2(myHex):
	ascii_string = ""
	for i in range (0, len(myHex), 2):
		hexPair = myHex[i:i+2]
		try:
			myChar = bytes.fromhex(hexPair).decode('utf-8')
		except:
			myChar = "?"
		ascii_string += myChar
		# print(hexPair, " ", myChar)
	# print(ascii_string)
	return ascii_string


def hexToStringAllStr(myHex):
	bytes_object = bytearray.fromhex(myHex) #Convert to bytes object
	ascii_string = bytes_object.decode('ASCII') #Convert to ASCII representation
	print(ascii_string)
	return ascii_string


# myHex = "10242400426F6E6A6F75720000000000000000D7F2"
# print()
# print(hexToStringBytes2(myHex.upper()))


# myHex = "424f4e4a4f5552"
# hexToStringBytes(myHex.upper())
# print()
# hexToStringAllStr(myHex.upper())

# myHex = "426f6e6a6f7572"
# hexToStringBytes(myHex.upper())
# print()
# hexToStringAllStr(myHex.upper())

# myHex = "7C4A0340A44A0340A44A0340A44A0340"
# hexToStringBytes(myHex.upper())

# myHex = "69616C697A696E6720455350206D6F64"
# hexToStringBytes(myHex.upper())

def fileHextoFileString(ifilename, ofilename):
	ifile = open(ifilename, 'r')
	lines = ifile.readlines()
	lineNb = 0;

	for line in lines :
		if (line[-1] == '\n'):
			line = line[:-1]
		line = line[9:-2]
		# print(line)
		lines[lineNb] = str(lineNb+1) + "   " + hexToStringBytes2(line.upper()) + '\n'
		# print(lines[lineNb])
		lineNb += 1

	ofile = open(ofilename, 'w')
	ofile.writelines(lines)
	ifile.close()
	ofile.close()


fileHextoFileString(ifilename, ofilename)
