class classinstallation:
	def __init__(self, InsLibelleVoie, InsTransportTrain, Nb_Equipements, InsPartLibelle, InsNbPlaceParkingHandi, InsNbPlaceParking, InsTransportBateau, InsNoVoie, InsLieuDit, InsTransportTram, InsEmpriseFonciere, Latitude, ComLib, InsTransportBus, InsCodePostal, InsMultiCommune, ComInsee, InsDateMaj, InsAccessibiliteAucun, lol, Nb_FicheEquipement, InsTransportAutre, InsAccessibiliteHandiSens, geo, InsGardiennee, InsTransportMetro, InsAccessibiliteHandiMoteur, InsNumeroInstall, Longitude):
		self.InsLibelleVoie = InsLibelleVoie
		self.InsTransportTrain = InsTransportTrain
		self.Nb_Equipements = Nb_Equipements
		self.InsPartLibelle = InsPartLibelle
		self.InsNbPlaceParkingHandi = InsNbPlaceParkingHandi
		self.InsNbPlaceParking = InsNbPlaceParking
		self.InsTransportBateau = InsTransportBateau
		self.InsNoVoie = InsNoVoie
		self.InsLieuDit = InsLieuDit
		self.InsTransportTram = InsTransportTram
		self.InsEmpriseFonciere = InsEmpriseFonciere
		self.Latitude = Latitude
		self.ComLib = ComLib
		self.InsTransportBus = InsTransportBus
		self.InsCodePostal = InsCodePostal
		self.InsMultiCommune = InsMultiCommune
		self.ComInsee = ComInsee
		self.InsDateMaj = InsDateMaj
		self.InsAccessibiliteAucun = InsAccessibiliteAucun
		self.lol = lol
		self.Nb_FicheEquipement = Nb_FicheEquipement
		self.InsTransportAutre = InsTransportAutre
		self.InsAccessibiliteHandiSens = InsAccessibiliteHandiSens
		self.geo = geo
		self.InsGardiennee = InsGardiennee
		self.InsTransportMetro = InsTransportMetro
		self.InsAccessibiliteHandiMoteur = InsAccessibiliteHandiMoteur
		self.InsNumeroInstall = InsNumeroInstall
		self.Longitude = Longitude

	def toString(self):
		print ("[" + self.InsLibelleVoie + " ; " + self.InsTransportTrain + " ; " + self.Nb_Equipements + " ; " + self.InsPartLibelle + " ; " + self.InsNbPlaceParkingHandi + " ; " + self.InsNbPlaceParking + " ; " + self.InsTransportBateau + " ; " + self.InsNoVoie + " ; " + self.InsLieuDit + " ; " + self.InsTransportTram + " ; " + self.InsEmpriseFonciere + " ; " + self.Latitude + " ; " + self.ComLib + " ; " + self.InsTransportBus + " ; " + self.InsCodePostal + " ; " + self.InsMultiCommune + " ; " + self.ComInsee + " ; " + self.InsDateMaj + " ; " + self.InsAccessibiliteAucun + " ; " + self.lol + " ; " + self.Nb_FicheEquipement + " ; " + self.InsTransportAutre + " ; " + self.InsAccessibiliteHandiSens + " ; " + self.geo + " ; " + self.InsGardiennee + self.InsTransportMetro + " ; " + self.InsAccessibiliteHandiMoteur + " ; " + self.InsNumeroInstall + " ; " + self.Longitude + "]\n\n")
