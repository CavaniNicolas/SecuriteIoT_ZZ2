# print("Bonjour".encode())
# print(type("Bonjour".encode()))

# r avant une chaine de caracteres desactive l'utilisation de \
#print(r"\h")

# _ est une variable autorisee en python, convention de nomage lorsque le compteur n'est pas utilise
#for _ in valeur

# Pour afficher 48 en hexa (avec 2 nombres hexa minimum)
#print("{:02x}".format(48))


def toCdecl(ch, prefix="char tab"):
	outp=list(ch)
	return prefix+"[{}]".format(len(outp)+1)+r"""="\x"""+(r"\x".join(["{:02x}".format(ord(_)) for _ in outp]))+r"""";"""

def toCdecl2(ch):
	outp=list(ch)
	return r"\x"+(r"\x".join(["{:02x}".format(ord(_)) for _ in outp]))+r""

def Xor(inp, key):
	keyL = len(key)
	return [chr(ord(inp[i]) ^ ord(key[i % keyL])) for i in range(len(inp))]

def Xor2(tabMessage, tabKey):
	keyL = len(tabKey)
	s = b""
	for i in range (len(tabMessage)):
		s += (bytes)(chr(ord(inp[i]) ^ ord(key[i % keyL])))


def EncodeXor(tabMessage,tabKey):
	return toCdecl2(Xor(tabMessage, tabKey))

def main1():
	xor = Xor("Bonjour", "A")
	print(xor)
	print(type(xor))
	print(list(xor))
	print(toCdecl(Xor("Bonjour", "A")))
	print(toCdecl2(Xor("Bonjour", "A")))
	print(bytes(toCdecl2(Xor("Bonjour", "A")), 'utf-8'))
	# b = b'\x03./+.43'
	# print (b)
	# print (type(b))

	print(ord("a"))
	print(ord('a'))
	print(chr(97))

	liste = Xor("Bonjour", "A")
	print (liste)
	ss = ""
	# for _ in range (len(liste)):
	ss = r"\x".join(["{:02x}".format(ord(_)) for _ in liste])

	print(ss)

	s = r"""="\h"""
	s += "y"
	print(s)

	res = chr(ord("B".encode())^ord("A".encode()))
	print(res)

	print("Bonjour".encode())
	xor = Xor("Bonjour", "A")
	print(xor.decode("utf-8", "backslashreplace"))
	# print(b'\x80abc'.decode("utf-8", "backslashreplace"))

def EncodeXor2(tabMessage,tabKey):
    """ Chiffrement Ou exclusif."""
    """ tabMessage contient le message sous forme de tableau d'octets"""
    """ tabKey contient la clef sous forme de tableau d'octets"""
    """ Retourne un tableau d'octets."""
    tabKey = tabKey * (len(tabMessage) // len(tabKey) + 1)
    return bytes([a^b for a,b in zip(tabMessage,tabKey)])

def main2():
	tabKey = "A".encode()
	print(tabKey*3)
	tabKey = tabKey * (len("Bonjour".encode()) // len(tabKey) + 1)
	print(tabKey)

	resTab = bytes(len(tabKey))
	print(resTab)

	resTab = bytes([a^b for a,b in zip("Bonjour".encode(), "AAAAAAAA".encode())])
	print(resTab)

	for a,b in zip("Bonjour".encode(), "AAAAAAAA".encode()):
		print(a^b, bytes([a^b]))
		print(a, bytes([a]))
		print(b, bytes([b]))

	print(EncodeXor2("Bonjour".encode(), "A".encode()))

	rList = [1, 2, 3, 4, 5]
	arr = bytes(rList)
	print(arr)

def Indice(table,element):
    """ Retourne l'indice d'élément dans table"""
    return table.index(element)

print( Indice([1, 2, 4, 5, 6, 3, 7, 3], 3))