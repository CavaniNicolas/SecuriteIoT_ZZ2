# -*- coding: utf-8 -*-
def EncodeXor(tabMessage, tabKey):
    """ Chiffrement Ou exclusif."""
    """ tabMessage contient le message sous forme de tableau d'octets"""
    """ tabKey contient la clef sous forme de tableau d'octets"""
    """ Retourne un tableau d'octets."""
    tabKey = tabKey * (len(tabMessage) // len(tabKey) + 1)
    resTab = bytes([a^b for a,b in zip(tabMessage, tabKey)])
    return resTab

def DecodeXor(tabMessage, tabKey):
    """ Chiffrement Ou exclusif."""
    """ tabMessage contient le message sous forme de tableau d'octets"""
    """ tabKey contient la clef sous forme de tableau d'octets"""
    """ Retourne un tableau d'octets."""
    tabKey = tabKey * (len(tabMessage) // len(tabKey) + 1)
    resTab = bytes([a^b for a,b in zip(tabMessage, tabKey)])
    return resTab

def Indice(table, element):
    """ Retourne l'indice du premier élément dans table"""
    return table.index(element)

def EncodeBase64(tabMessage):
    """ Encode en base 64 le paramètre chaine"""
    """ tabMessage contient le message sous forme de tableau d'octets"""
    """ Retourne un tableau d'octets."""
    import base64
    return base64.b64encode(tabMessage)

def DecodeBase64(strMessage):
    """ Decode la chaine encodée en base 64"""
    """ strMessage doit être une chaine ASCII elle sera encodée en utf-8"""
    """ retourne un tableau d'octets"""
    import base64
    return base64.b64decode(strMessage.encode())

def EncodeAES_ECB(strMessage, tabKey):
    """ Chiffrement AES-ECB 128 bits de strMessage avec tabKey comme clef.
        La taille de chaine est quelconque et sera complétée par des
        caractères espace si nécessaire. tabKey est un tableau 16 éléments.
        Avant chiffrement la chaine est encodée en utf8 """
    from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
    from cryptography.hazmat.backends import default_backend
    import os

    key=bytes(tabKey)
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    strMessage=(strMessage+" "*16)[:16]
    ct = encryptor.update(strMessage.encode("utf-8")) + encryptor.finalize()
    return ct

def DecodeAES_ECB(tabMessage, tabKey):
    """ Dechiffrement AES ECB de tabMessage. La clef tabKey est un tableau de 16 éléments.
        Retourne un tableau d'octets. Les caractères espace en fin de
        tableau sont supprimés."""
    from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
    from cryptography.hazmat.backends import default_backend
    import os

    key=bytes(tabKey)
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    dt = decryptor.update(tabMessage) + decryptor.finalize()
    return dt

def Contient(aiguille, chaine):
    """ Resultat True si le paramètre chaine contient la chaine aiguille."""
    return aiguille in chaine

def EstImprimable(caractere):
    """ Liste des caractères imprimables :
        0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """
    import string
    return caractere in string.printable

def Remplace(chaine,avant,apres):
    """ Remplace les occurrences de avant par apres dans chaine."""
    return chaine.replace(avant,apres)

def Extraire(chaine,separation,n):
    """ Retourne la valeur du nième champ de chaine.
        Les champs sont séparés par le caractÃ¨re séparation."""
    return int(chaine.split(separation)[n])

def Format(n):
    """ Retourne une chaine de caractères de 4 caractères pour tout nombre entier de 0 à  9999
        Les valeurs seront précédées de 0."""
    return "{:04}".format(n)

def toTab(strMessage):
    """ Encode une chaine en tableau d'octets. l'encodage utilisé est "utf-8"""
    return strMessage.encode()

def toStr(strMessage):
    """Decode un tableau d'octets en chaine utf-8"""
    return strMessage.decode()


def DecodeXorBase64(tabMessage, tabKey):
    decodedXor = DecodeXor(tabMessage, tabKey)
    return DecodeBase64(toStr(decodedXor))


print ( "\n%%%%%%%%%%%%%%%%%%%%% base 64 %%%%%%%%%%%%%%%%%%%" )
payload = "\x0c\x1fc`!drq\n\x02\n\x1c\x02\x0b\x19\x17v\x18\x10\x18\x0e\x10\x19\x0b\x05d\n\x02\n\x1c\x02\x0b"
payload = toTab(payload)
print( payload )

encodedPayload = EncodeBase64(payload)
print( encodedPayload )
encodedPayload = toStr(encodedPayload)

# encodedPayload = "DBcFcXIzdmRjYXVlDB8PFAEcG2QUCRUUAQUbBARpcAI="
# print( DecodeBase64 (encodedPayload))
encodedPayload = "DBcFcXIzdmRjYXVlDB8PFAEcG2QUCRUUAQUbBARpcAI="
print( DecodeBase64 (encodedPayload))
# encodedPayload = "DBcFcXIzdmRjYXVlDB8PFAEcG2QUCRUUAQUbBARpcAI="
# print( toStr(DecodeBase64 (encodedPayload)))


# encodedPayload = "DCyLUj2Nd"
# print( toStr(DecodeBase64 (encodedPayload)))

payload = "ISIMAZZF5"
# payload = toTab(payload)
# encodedPayload = EncodeBase64(payload)
# print( encodedPayload )

# print (DecodeBase64(' a".,1-$5$3'))




def ContientLettreALettre(aiguille, chaine):
    isIn = True
    for i in range (len(aiguille)):
        """ Resultat True si le paramètre chaine contient la chaine aiguille."""
        isIn = Contient(aiguille[i], chaine)
    return isIn

# payload en bytes
def XorBrutForce(payload):
    tabKeys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range (len(tabKeys)):
        print (tabKeys[i])
        xorDecoded = DecodeXor(payload, tabKeys[i])
        """ Resultat True si le paramètre chaine contient la chaine aiguille."""
        if (ContientLettreALettre(xorDecoded, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ")):
            tabRes.append(xorDecoded)
    return len(tabRes)


print ( "\n%%%%%%%%%%%%%%%%%%%%% Xor %%%%%%%%%%%%%%%%%%%" )
key = toTab("CQ")
print (key)

# payload = toTab("\x0c\x17\x05qr3vdcaue\x0c\x1f\x0f\x14\x01\x1c\x1bd\x14\t\x15\x14\x01\x05\x1b\x04\x04ip\x02")
# print( payload )

payload = toTab("ON 1b51 ISIMAZZF5ISIMAZZF5ISIMAZ")

print(DecodeXor(payload, key))

# XorBrutForce(payload)





# print ( "\n%%%%%%%%%%%%%%%%%%%% Xor puis base 64 %%%%%%%%%%%%%%%%%%%" )
# key = toTab("A")
# print (key)

# payload = toTab("bkb4QbELVEOH9ZD285fzQ")
# print( payload )
# print (DecodeXorBase64(payload, key))


# print ( "\n%%%%%%%%%%%%%%%%%%%%% AES %%%%%%%%%%%%%%%%%%%" )
# keyTab = [161, 216, 149, 60, 177, 180, 108, 234, 176, 12, 149, 45, 255, 157, 80, 136]
# encodedAES = EncodeAES_ECB("ON/ISIMA/ON/LED1/LED2", keyTab)
# print(encodedAES)
# decodedAES = DecodeAES_ECB(encodedAES, keyTab)
# print(decodedAES)



