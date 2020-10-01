
def checksumFile(filename):
    filin = open(filename,'r')
    lignes = filin.readlines()
    i_ligne = 0

    for ligne in lignes :
        sum = 0
        i_start = 1

        if ligne[-1] == '\n':
            ligne = ligne[:-1]
        length = len(ligne)-2

        for i_end in range(3,length+1,2):
            sum += int(ligne[i_start:i_end],16)
            i_start += 2

        sum_inv = sum ^ 0xFF
        CC = hex(sum_inv+1)
        CC = CC[2:].upper()
        lignes[i_ligne] = ligne[:-2] + CC + '\n'

        i_ligne += 1
    
    print(lignes)

    filout = open(filename,'w')
    filout.writelines(lignes)     
    filin.close()
    filout.close()

checksumFile("hex.txt")