def DecodeBase64(strMessage):
    """ Decode la chaine encodée en base 64"""
    """ strMessage doit être une chaine ASCII elle sera encodée en utf-8"""
    """ retourne un tableau d'octets"""
    import base64
    return base64.b64decode(strMessage.encode())

def toStr(strMessage):
    """Decode un tableau d'octets en chaine utf-8"""
    return strMessage.decode()

ifile = open("captureNetdefi5.log", 'r')
lines = ifile.readlines()
lineNb = 0;

for line in lines :
    line = toStr(DecodeBase64(line))
    lines[lineNb] = line + "\n"
    lineNb += 1

ofile = open("BASE64captureNetdefi5.log", 'w')
ofile.writelines(lines)
ifile.close()
ofile.close()
