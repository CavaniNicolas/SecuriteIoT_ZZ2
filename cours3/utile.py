
def inverserChaine(chaine):
	invChaine = ""
	for i in range (1, len(chaine)+1):
		invChaine += chaine[-i]
	print(invChaine)

inverserChaine("bon5jour")

