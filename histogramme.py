import sys
import csv
import matplotlib.pyplot as plt

def histogramme(fileName) : 
	GR = [] # gains relatifs 
	with open(fileName+".csv") as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			gr = row[0]
			GR.append(float(gr))
	lg = len(GR)
	print(str(lg)+" valeurs dans le fichier des gains relatifs")
	lz = len([z for z in GR if z == 0.0])
	print(str(lz)+" valeurs 0.0 dans le fichier des gains relatifs")
	# Enlever les 0 car ils écrasent l'histogramme
	GR = [g for g in GR if g != 0.0]
	lg = len(GR)
	print(str(lg)+" valeurs non nulles dans le fichier des gains relatifs")
	print("valeur non nulle minimum : " + str(min(GR)))
	print("valeur non nulle maximum : " + str(max(GR)))
	print("creation de l'histogramme des valeurs non nulles de gain relatif")
	h = plt.hist(GR,bins=int(lg/10)) #  nombre de bins à votre convenance...
	plt.savefig(fileName+".png")
	plt.close()
	csvfile.close

def main() : 
	if len(sys.argv) != 2 :
		print("Usage : python3 histogramme.py fileName")
		print("Exemple : python3 hystogramme.py DR")
		return
	fileName = sys.argv[1]
	histogramme(fileName)
	print("l'histogramme est dans le fichier " + fileName + ".png")

main()