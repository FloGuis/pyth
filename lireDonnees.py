import json
import classactivite
import classinstallation
import classequipement

def lectureDonneesJSon(fichier):
	import json
	file = open(fichier)
	jr = json.load(file)
	donnee0 = json.dumps(jr, indent=4)
#	donnee1 = donnee0.split("{")
	print (donnee0)

#	for classe in jr["data"]:
#		act = classactivite.classactivite(classe["ActCode"], classe["EquNbEquIdentique"], classe["EquActivitePratique"], classe["EquActiviteSalleSpe"], classe["ComInsee"], classe["ActNivLib"], classe["EquipementId"], classe["ActLib"], classe["EquActivitePraticable"], classe["ComLib"])
#		print (act.toString())
#	for classe in jr["data"]:
#		inst = classinstallation.classinstallation(classe["InsLibelleVoie"], classe["InsTransportTrain"], classe["Nb_Equipements"], classe["InsPartLibelle"], classe["InsNbPlaceParkingHandi"], classe["InsNbPlaceParking"] , classe["InsTransportBateau"], classe["InsNoVoie"], classe["InsLieuDit"], classe["InsTransportTram"], classe["InsEmpriseFonciere"], classe["Latitude"], classe["ComLib"], classe["InsTransportBus"], classe["InsCodePostal"], classe["InsMultiCommune"], classe["ComInsee"], classe["InsDateMaj"], classe["InsAccessibiliteAucun"], classe["_l"], classe["Nb_FicheEquipement"], classe["InsTransportAutre"], classe["InsAccessibiliteHandiSens"], classe["geo"], classe["InsGardiennee"], classe["InsTransportMetro"], classe["InsAccessibiliteHandiMoteur"], classe["InsNumeroInstall"], classe["Longitude"])
#		print (inst.toString())
		#for attribut in classe:
			# str(classe[attribut]) + "\n"
		

lectureDonneesJSon('/hometu/etudiants/E133926X/workspace/Python/Donneesinstall.json')
#lectureDonneesJSon('/hometu/etudiants/E133926X/workspace/Python/Donneesact.json')
#lectureDonneesJSon('/hometu/etudiants/E133926X/workspace/Python/Donneesequip.json')
#lectureDonneesJSon('/hometu/etudiants/E133926X/workspace/pyth/equipement_fixed.json')
