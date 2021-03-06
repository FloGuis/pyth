import cherrypy
import json
import sqlite3
 
data = json.loads(open("/hometu/etudiants/E133926X/workspace/pyth/Donneesact.json").read())
table = '''installation'''
ville = ""

class WebManager(object):
	"""
	Exposes web services
	"""

	@cherrypy.expose
	def index(self):
		"""
		Exposes the service at localhost:8080/
		"""
		conn = sqlite3.connect('lepythonenbd.db')
		c = conn.cursor()
		res = 0
		for row in c.execute('''Select * from ''' + table + ''' order by ComInsee'''):
			res = res + 1
		reponse = "<p>There are {0} items.</p>".format(res)
		reponse = reponse +'''
				<script>
					function envoi()
					{
						inputtable = document.getElementById("inputtable").value;
						inputville = document.getElementById("inputville").value;
						location.href="search/" + inputtable; // + "$" + inputville + "/";
					}
				</script>
				<label for="inputtable">Table : </label><input type="text" name="inputtable" id="inputtable" /><br />
				<label for="inputville">Ville : </label><input type="text" name="inputville" id="inputville" /><br />
				<button value="Rechercher" onclick="envoi()">Envoyer</button>
			'''
		return reponse
	 
	@cherrypy.expose
	def show_all(self):
		"""
		Exposes the service at localhost:8080/show_all/
		"""
		conn = sqlite3.connect('lepythonenbd.db')
		c = conn.cursor()
		res = "<a href='..'>Retour à la page d'accueil</a><br /><br /><table border='1px solid black'><tr><th>"
		i = 0
		if (table == '''activite'''):
			res = res + "ActCode</th><th>EquNbEquIdentique</th><th>EquActivitePratique</th><th>EquActiviteSalleSpe</th><th>ComInsee</th><th>ActNivLib</th><th>EquipementId</th><th>ActLib</th><th>EquActivitePraticable</th><th>ComLib</th></tr>"
		elif (table == '''equipement'''):
			res = res + "EquSanitaireSportif</th><th>EquErpPA</th><th>EquEclairage</th><th>EquHauteurEvolution</th><th>EquNatSurfaceBassin</th><th>EquNatureAcPubRout</th><th>EquSurfaceEvolution</th><th>EquNatLongueurBassin</th><th>EquSono</th><th>GestionTypeProprietaireSecLib</th><th>EquConfortSolarium</th><th>EquNatTobog</th><th>EquNatNbT1</th><th>EquUtilAutre</th><th>EquTravauxRealVetuste</th><th>EquNatNbT3</th><th>EquNatSurv</th><th>EquConfortAutre</th><th>EquNatSonorisationSub</th><th>EquErpCategorie</th><th>EquAccesHandisAire</th><th>EquAccueilReception</th><th>EquAccueilBuvette</th><th>GestionTypeProprietairePrincLib</th><th>NatureLibelle</th><th>EquDateMaj</th><th>EquAccueilAutre</th><th>EquHauteurSurfaceEvo</th><th>EquNatFormeLib</th><th>EquAccesHandisAucun</th><th>EquErpOA</th><th>EquDouche</th><th>EquAccesHandimVestiaire</th><th>EquNatEclSub</th><th>EquNatureLocPed</th><th>EquVestiaireSpoChauffe</th><th>EquNatureSignal</th><th>EquNom</th><th>EquChauffageAutre</th><th>EquAccesHandisVestiaire</th><th>EquAccueilAucun</th><th>EquipementTirPlateau</th><th>EquipementTir50</th><th>EquAthNBMarteauMixte</th><th>EquUtilIndividuel</th><th>ComInsee</th><th>EquConfortBainBouillonant</th><th>EquNatNbP10</th><th>EquOuvertSaison</th><th>EquNatProfMax</th><th>EquNatureAcPubPed</th><th>EquTableauFixe</th><th>InsNom</th><th>EquGestionDSP</th><th>EquNbVestiaireSpo</th><th>EquNatureSKTotalRemontee</th><th>EquTravauxRealDegradation</th><th>EquAthNbCouloirLigne</th><th>EquAccueilDopage</th><th>EquAccesHandimAire</th><th>EquChrono</th><th>GestionTypeGestionnairePrincLib</th><th>EquUtilFormation</th><th>EquNatureAcSecPed</th><th>EquSaeNbCouloir</th><th>EquNatProfMini</th><th>EquAthDev</th><th>EquSaeHauteur</th><th>EquAccueilBureau</th><th>EquAthNbJavelot</th><th>InsNumeroInstall</th><th>EquAnneeService</th><th>EquAthNbSautPerche</th><th>EquNatCouloir</th><th>EquipementTir300</th><th>EquAccesHandimAucun</th><th>EquNatureAcSecRout</th><th>EquipementTir200</th><th>EquGpsX</th><th>EquNomBatiment</th><th>EquipementTir100</th><th>EquGpsY</th><th>EquLargeurEvolution</th><th>EquChauffageNon</th><th>GestionTypeGestionnaireSecLib</th><th>EquAthNbSautHauteur</th><th>EquDateDernierTravauxReal</th><th>EquipementId</th><th>EquUtilScolaire</th><th>EquNatureAutorise</th><th>EquSanitairePublic</th><th>EquAccueilInfirmerie</th><th>EquAccueilClub</th><th>EquChauffageSolaire</th><th>EquAthNbSautTriple</th><th>EquNatNbTTotal</th><th>EquProximite</th><th>EquipNatureSituationLib</th><th>EquChauffageFuel</th><th>EquipementTypeLib</th><th>EquDateDernierTravauxAucun</th><th>EquErpREF</th><th>EquipementTir25</th><th>EquAthNbDisque</th><th>EquAmenagementAucun</th><th>AnneeTravauxRealLibelle</th><th>EquAccesHandimSaniSpo</th><th>EquNbCouloirPiste</th><th>EquChauffageElectricite</th><th>EquNatNbP3</th><th>EquNatureClassFedeMaxi</th><th>EquAccesHandimTribune</th><th>FamilleFicheLib</th><th>EquNatNbPTotal</th><th>EquTravauxRealNorme</th><th>EquErpCTS</th><th>EquAthRiviere</th><th>EquAccesHandisTribune</th><th>EquipementFiche</th><th>NatureSolLib</th><th>EquNatSurfacePlageBassin</th><th>EquNatureESTour</th><th>EquipementTir10</th><th>ComLib</th><th>EquAccueilMedic</th><th>AnneeServiceLib</th><th>EquNatAutre</th><th>EquNaturePDESI</th><th>EquNatRiviere</th><th>EquNatureAlert</th><th>EquNatNbP7</th><th>EquNatureAcPubMec</th><th>EquNatNbP5</th><th>EquNatLargeurBassin</th><th>EquErpSG</th><th>EquNatureClassFedeMini</th><th>EquAccueilLocalRangement</th><th>EquNatureAcPubNau</th><th>EquConfortSauna</th><th>EquLongueurEvolution</th><th>EquAccesHandisSaniSpo</th><th>EquNbPlaceTribune</th><th>EquConfortBainVapeur</th><th>EquAthNbSautTotal</th><th>EquNatureAcSecNau</th><th>EquTravauxRealUsager</th><th>EquNbEquIdentique</th><th>EquUtilRecreation</th><th>EquAthNbPoids</th><th>EquNatFM</th><th>EquAccueilSalle</th><th>EquNatImHandi</th><th>EquNatMaV</th><th>EquNatureAcSecMec</th><th>EquAthNbCouloirHorsLigne</th><th>EquipementTirAutre</th><th>EquDemarcheHQE</th><th>EquTravauxRealConformite</th><th>EquNatureAETreuil</th><th>EquNbVestiaireArbitre</th><th>EquAthNbSautLongueur</th><th>EquAthNbLancerTotal</th><th>EquNatureSEVoies</th><th>EquAccesHandisSaniPub</th><th>EquErpRPE</th><th>EquNatMM</th><th>EquAthLongLigneDroite</th><th>EquErpX</th><th>EquConfortAucun</th><th>EquErpR</th><th>EquChauffageGaz</th><th>EquErpO</th><th>EquSaeSurface</th><th>EquErpN</th><th>EquPresencePataugeoir</th><th>EquNatPentaglisse</th><th>EquUtilPerformance</th><th>EquNatureLocTec</th><th>EquErpP</th><th>EquAccesHandimSaniPub</th><th>EquUtilClub</th><th>EquAthNbMarteau</th><th>EquErpL</th></tr>"
		elif (table == '''installation'''):
			res = res + "InsLibelleVoie</th><th>InsTransportTrain</th><th>Nb_Equipements</th><th>InsPartLibelle</th><th>InsNbPlaceParkingHandi</th><th>InsNbPlaceParking</th><th>InsTransportBateau</th><th>InsNoVoie</th><th>InsLieuDit</th><th>InsTransportTram</th><th>InsEmpriseFonciere</th><th>Latitude</th><th>ComLib</th><th>InsTransportBus</th><th>InsCodePostal</th><th>InsMultiCommune</th><th>ComInsee</th><th>InsDateMaj</th><th>InsAccessibiliteAucun</th><th>Nb_FicheEquipement</th><th>InsTransportAutre</th><th>InsAccessibiliteHandiSens</th><th>InsGardiennee</th><th>InsTransportMetro</th><th>InsAccessibiliteHandiMoteur</th><th>InsNumeroInstall</th><th>Longitude</th></tr>"
		else:
			res = res + "</th></tr>"

		for row in c.execute('''Select * from ''' + table + ''' order by ComInsee'''):
			res = res + "<tr>"
			if (int(i) <= int(100)):
				for line in row:
					res = res + "<td>" + str(line) + "</td>"
				res = res + "</tr>"
			i = i + 1
		res = res + "<tr></tr></table>"
		return res
	 
	@cherrypy.expose
	def show(self, id):
		"""
		Exposes the service at localhost:8080/show/[id]/
		"""
		conn = sqlite3.connect('lepythonenbd.db')
		c = conn.cursor()
		res = "<a href='..'>Retour à la page d'accueil</a><br /><br /><table border='1px'><tr>"
		i = 0
		res = res + "<th>"
		if (table == '''activite'''):
			res = res + "ActCode</th><th>EquNbEquIdentique</th><th>EquActivitePratique</th><th>EquActiviteSalleSpe</th><th>ComInsee</th><th>ActNivLib</th><th>EquipementId</th><th>ActLib</th><th>EquActivitePraticable</th><th>ComLib</th></tr>"
		elif (table == '''equipement'''):
			res = res + "EquSanitaireSportif</th><th>EquErpPA</th><th>EquEclairage</th><th>EquHauteurEvolution</th><th>EquNatSurfaceBassin</th><th>EquNatureAcPubRout</th><th>EquSurfaceEvolution</th><th>EquNatLongueurBassin</th><th>EquSono</th><th>GestionTypeProprietaireSecLib</th><th>EquConfortSolarium</th><th>EquNatTobog</th><th>EquNatNbT1</th><th>EquUtilAutre</th><th>EquTravauxRealVetuste</th><th>EquNatNbT3</th><th>EquNatSurv</th><th>EquConfortAutre</th><th>EquNatSonorisationSub</th><th>EquErpCategorie</th><th>EquAccesHandisAire</th><th>EquAccueilReception</th><th>EquAccueilBuvette</th><th>GestionTypeProprietairePrincLib</th><th>NatureLibelle</th><th>EquDateMaj</th><th>EquAccueilAutre</th><th>EquHauteurSurfaceEvo</th><th>EquNatFormeLib</th><th>EquAccesHandisAucun</th><th>EquErpOA</th><th>EquDouche</th><th>EquAccesHandimVestiaire</th><th>EquNatEclSub</th><th>EquNatureLocPed</th><th>EquVestiaireSpoChauffe</th><th>EquNatureSignal</th><th>EquNom</th><th>EquChauffageAutre</th><th>EquAccesHandisVestiaire</th><th>EquAccueilAucun</th><th>EquipementTirPlateau</th><th>EquipementTir50</th><th>EquAthNBMarteauMixte</th><th>EquUtilIndividuel</th><th>ComInsee</th><th>EquConfortBainBouillonant</th><th>EquNatNbP10</th><th>EquOuvertSaison</th><th>EquNatProfMax</th><th>EquNatureAcPubPed</th><th>EquTableauFixe</th><th>InsNom</th><th>EquGestionDSP</th><th>EquNbVestiaireSpo</th><th>EquNatureSKTotalRemontee</th><th>EquTravauxRealDegradation</th><th>EquAthNbCouloirLigne</th><th>EquAccueilDopage</th><th>EquAccesHandimAire</th><th>EquChrono</th><th>GestionTypeGestionnairePrincLib</th><th>EquUtilFormation</th><th>EquNatureAcSecPed</th><th>EquSaeNbCouloir</th><th>EquNatProfMini</th><th>EquAthDev</th><th>EquSaeHauteur</th><th>EquAccueilBureau</th><th>EquAthNbJavelot</th><th>InsNumeroInstall</th><th>EquAnneeService</th><th>EquAthNbSautPerche</th><th>EquNatCouloir</th><th>EquipementTir300</th><th>EquAccesHandimAucun</th><th>EquNatureAcSecRout</th><th>EquipementTir200</th><th>EquGpsX</th><th>EquNomBatiment</th><th>EquipementTir100</th><th>EquGpsY</th><th>EquLargeurEvolution</th><th>EquChauffageNon</th><th>GestionTypeGestionnaireSecLib</th><th>EquAthNbSautHauteur</th><th>EquDateDernierTravauxReal</th><th>EquipementId</th><th>EquUtilScolaire</th><th>EquNatureAutorise</th><th>EquSanitairePublic</th><th>EquAccueilInfirmerie</th><th>EquAccueilClub</th><th>EquChauffageSolaire</th><th>EquAthNbSautTriple</th><th>EquNatNbTTotal</th><th>EquProximite</th><th>EquipNatureSituationLib</th><th>EquChauffageFuel</th><th>EquipementTypeLib</th><th>EquDateDernierTravauxAucun</th><th>EquErpREF</th><th>EquipementTir25</th><th>EquAthNbDisque</th><th>EquAmenagementAucun</th><th>AnneeTravauxRealLibelle</th><th>EquAccesHandimSaniSpo</th><th>EquNbCouloirPiste</th><th>EquChauffageElectricite</th><th>EquNatNbP3</th><th>EquNatureClassFedeMaxi</th><th>EquAccesHandimTribune</th><th>FamilleFicheLib</th><th>EquNatNbPTotal</th><th>EquTravauxRealNorme</th><th>EquErpCTS</th><th>EquAthRiviere</th><th>EquAccesHandisTribune</th><th>EquipementFiche</th><th>NatureSolLib</th><th>EquNatSurfacePlageBassin</th><th>EquNatureESTour</th><th>EquipementTir10</th><th>ComLib</th><th>EquAccueilMedic</th><th>AnneeServiceLib</th><th>EquNatAutre</th><th>EquNaturePDESI</th><th>EquNatRiviere</th><th>EquNatureAlert</th><th>EquNatNbP7</th><th>EquNatureAcPubMec</th><th>EquNatNbP5</th><th>EquNatLargeurBassin</th><th>EquErpSG</th><th>EquNatureClassFedeMini</th><th>EquAccueilLocalRangement</th><th>EquNatureAcPubNau</th><th>EquConfortSauna</th><th>EquLongueurEvolution</th><th>EquAccesHandisSaniSpo</th><th>EquNbPlaceTribune</th><th>EquConfortBainVapeur</th><th>EquAthNbSautTotal</th><th>EquNatureAcSecNau</th><th>EquTravauxRealUsager</th><th>EquNbEquIdentique</th><th>EquUtilRecreation</th><th>EquAthNbPoids</th><th>EquNatFM</th><th>EquAccueilSalle</th><th>EquNatImHandi</th><th>EquNatMaV</th><th>EquNatureAcSecMec</th><th>EquAthNbCouloirHorsLigne</th><th>EquipementTirAutre</th><th>EquDemarcheHQE</th><th>EquTravauxRealConformite</th><th>EquNatureAETreuil</th><th>EquNbVestiaireArbitre</th><th>EquAthNbSautLongueur</th><th>EquAthNbLancerTotal</th><th>EquNatureSEVoies</th><th>EquAccesHandisSaniPub</th><th>EquErpRPE</th><th>EquNatMM</th><th>EquAthLongLigneDroite</th><th>EquErpX</th><th>EquConfortAucun</th><th>EquErpR</th><th>EquChauffageGaz</th><th>EquErpO</th><th>EquSaeSurface</th><th>EquErpN</th><th>EquPresencePataugeoir</th><th>EquNatPentaglisse</th><th>EquUtilPerformance</th><th>EquNatureLocTec</th><th>EquErpP</th><th>EquAccesHandimSaniPub</th><th>EquUtilClub</th><th>EquAthNbMarteau</th><th>EquErpL</th></tr>"
		elif (table == '''installation'''):
			res = res + "InsLibelleVoie</th><th>InsTransportTrain</th><th>Nb_Equipements</th><th>InsPartLibelle</th><th>InsNbPlaceParkingHandi</th><th>InsNbPlaceParking</th><th>InsTransportBateau</th><th>InsNoVoie</th><th>InsLieuDit</th><th>InsTransportTram</th><th>InsEmpriseFonciere</th><th>Latitude</th><th>ComLib</th><th>InsTransportBus</th><th>InsCodePostal</th><th>InsMultiCommune</th><th>ComInsee</th><th>InsDateMaj</th><th>InsAccessibiliteAucun</th><th>Nb_FicheEquipement</th><th>InsTransportAutre</th><th>InsAccessibiliteHandiSens</th><th>InsGardiennee</th><th>InsTransportMetro</th><th>InsAccessibiliteHandiMoteur</th><th>InsNumeroInstall</th><th>Longitude</th></tr>"
		else:
			res = res + "</th></tr>"
		res = res + "</th></tr><tr>"
		for row in c.execute('''Select * from ''' + table + ''' order by ComInsee'''):
			if (int(i) == int(id)):
				for line in row:
					res = res + "<td>" + str(line) + "</td>"
				break
			i = i + 1
		res = res + "</tr></table>"
		return res
	

	@cherrypy.expose
	def search(self, request):
		"""
		Exposes the service at localhost:8080/search/[request]/
		"""
		requete = request.split("$")
		table = requete[0]
		ville = requete[1]
		return "<script>location.href='../show_all';</script>"

cherrypy.quickstart(WebManager())
