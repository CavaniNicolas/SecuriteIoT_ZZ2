a = "10455000068183207F0FE07FC0210501301C40369B"
b = "10455000068183207F0FF07FC0210501301C40369B"
c = "10242400426F6E6A6F7572000000000000000000F2"
d = "10242400426F6E6A6F75720000000000000000D7F2"

def correctChecksum (linHex):
	n = len(linHex) - 2
	s = 0

	for i in range(0, n-1, 2):
		s += int(linHex[i:i+2], 16)

	s = bin(s)
	sumcomp = ""

	for i in range(2, len(s)):
		if s[i] == "0":
			sumcomp += "1"
		if s[i] == "1":
			sumcomp += "0"

	print(s)
	print("b", sumcomp)
	print((int(sumcomp, 2)))
	print((int(sumcomp, 2) + 1) % 256)

	CC = hex((int(sumcomp, 2) + 1) % 256)
	print(CC)
	resLinHex = linHex[0:n] + CC[2:4]

	return resLinHex

# print(correctChecksum(a).upper())
# print(correctChecksum(b).upper())
print(correctChecksum(c).upper())
print(correctChecksum(d).upper())
