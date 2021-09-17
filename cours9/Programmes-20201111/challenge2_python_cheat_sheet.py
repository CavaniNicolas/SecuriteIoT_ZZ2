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

def main():
    """ Tests, toutes les lignes sont correctes (résultat : True). Complèter les fonctions."""
    import sys
    print (sys.version)

    print (EncodeXor("Bonjour".encode(),"A".encode())==b'\x03./+.43')
    print (DecodeXor(b"\n'..-","B".encode()).decode()=="Hello")
    print (EncodeXor(b"GoodBye",b"ABA")==b'\x06-.%\x008$')
    print (DecodeXor(b'\x0e42;8',b"ZWZ")=="Tchao".encode())
    print (Indice([1,2,3,4,5,6],3)==2)
    print (EncodeBase64(b"Une Chaine")==b"VW5lIENoYWluZQ==")
    print (DecodeBase64("VW5lIENoYWluZQ==")==b"Une Chaine")
    print (EncodeAES_ECB("Elements",[161, 216, 149, 60, 177, 180, 108, 234, 176, 12, 149, 45, 255, 157, 80, 136])==b'Z\xf5T\xef\x9f\x8bg\x15\xb3E\xe7&gm\x96\x1d')
    print (DecodeAES_ECB(b'Z\xf5T\xef\x9f\x8bg\x15\xb3E\xe7&gm\x96\x1d',[161, 216, 149, 60, 177, 180, 108, 234, 176, 12, 149, 45, 255, 157, 80, 136]).strip()==b"Elements")
    print (Contient("OK","Le resultat est OK !")==True)
    print (Contient("OK","Le resultat est Ok !")==False)
    print (EstImprimable("A")==True)
    print (EstImprimable("\x07")==False)
    print (EstImprimable(" ")==True)
    print (Remplace("Ceci est une string typique","string","chaine")=="Ceci est une chaine typique")
    print (Extraire("ROUGE,0034,4EF563",",",1)==34)
    print (Format(3)=="0003")
    print (Format(123)=="0123")
    print (toStr(b"\x41\x42")=="AB")
    print (toTab("CD")==b"\x43\x44")
    return

def cleanup():
    import shutil
    import os
    print (os.path.basename(__file__))
    f=os.path.basename(__file__)
    dir=os.path.dirname(__file__)
    fn=os.path.splitext(f)
    ext=fn[1]
    fn=fn[0]
    fn=fn+"_todo"
    f=fn+ext

    fn=open(f,"w")

    infunc=False;clean=False;ret=False;main=False;comm=False;frm=False
    for l in open(__file__,"r"):
        if ret:
            infunc=False;clean=False;ret=False;frm=False
            main=False
        if "from" in l:
            frm=True
        if "def" in l:
            infunc=True
            if "main" in l:
                main=True
        if "RETURN".lower() in l:
            ret=True
        if "CLEANUP".lower() in l:
            clean=True
        write=True
        if infunc:
            write=False
            #fn.write("infunc ")
            if "def" in l:
                write=True
            if l.count('"""')==1:
                comm=not comm
                write=True
            if comm:
                write=True
            if l.count('"""')==2:
                write=True
            if frm:
                write=False

        if clean:
            write=False
        if main:
            write=True
        if write:
            fn.write(l)
    fn.close()
    return

if __name__ == '__main__':
    print(EncodeXor(b"/ISIMA/SECRET_YIDIISTSA/CHALLENGE_1/DEFI_6/GROUPE_XX/LEDS/#",b"XORKEYDESPROFS"))
    main()
    cleanup()



