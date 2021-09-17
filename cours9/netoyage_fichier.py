ifile = open("capturedefi5.log", 'r')
lines = ifile.readlines()
lineNb = 0;

for line in lines :
    line = line[-13:-1]
    lines[lineNb] = line + "\n"
    lineNb += 1

ofile = open("captureNetdefi5.log", 'w')
ofile.writelines(lines)
ifile.close()
ofile.close()
