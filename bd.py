import json
import sqlite3
import classactivite

datainstall = json.load(open('/hometu/etudiants/E133926X/workspace/pyth/Donneesinstall.json'))
dataact = json.load(open('/hometu/etudiants/E133926X/workspace/pyth/Donneesact.json'))
dataequip = json.load(open('/hometu/etudiants/E133926X/workspace/pyth/Donneesequip.json'))

conn = sqlite3.connect('lepythonenbd.db')

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS installation")
c.execute('''CREATE TABLE installation (InsLibelleVoie text, InsTransportTrain text, Nb_Equipements text, InsPartLibelle text, InsNbPlaceParkingHandi text, InsNbPlaceParking text, InsTransportBateau text, InsNoVoie text, InsLieuDit text, InsTransportTram text, InsEmpriseFonciere text, Latitude text, ComLib text, InsTransportBus text, InsCodePostal text, InsMultiCommune text, ComInsee text, InsDateMaj text, InsAccessibiliteAucun text, Nb_FicheEquipement text, InsTransportAutre text, InsAccessibiliteHandiSens text, InsGardiennee text, InsTransportMetro text, InsAccessibiliteHandiMoteur text, InsNumeroInstall text, Longitude text)''')

c.execute("DROP TABLE IF EXISTS activite")
c.execute('''CREATE TABLE activite (ActCode text, EquNbEquIdentique text, EquActivitePratique text, EquActiviteSalleSpe text, ComInsee text, ActNivLib text, EquipementId text, ActLib text, EquActivitePraticable text, ComLib text)''')

c.execute("DROP TABLE IF EXISTS equipement")
c.execute('''CREATE TABLE equipement (EquSanitaireSportif text, EquErpPA text, EquEclairage text, EquHauteurEvolution text, EquNatSurfaceBassin text, EquNatureAcPubRout text, EquSurfaceEvolution text, EquNatLongueurBassin text, EquSono text, GestionTypeProprietaireSecLib text, EquConfortSolarium text, EquNatTobog text, EquNatNbT1 text, EquUtilAutre text, EquTravauxRealVetuste text, EquNatNbT3 text, EquNatSurv text, EquConfortAutre text, EquNatSonorisationSub text, EquErpCategorie text, EquAccesHandisAire text, EquAccueilReception text, EquAccueilBuvette text, GestionTypeProprietairePrincLib text, NatureLibelle text, EquDateMaj text, EquAccueilAutre text, EquHauteurSurfaceEvo text, EquNatFormeLib text, EquAccesHandisAucun text, EquErpOA text, EquDouche text, EquAccesHandimVestiaire text, EquNatEclSub text, EquNatureLocPed text, EquVestiaireSpoChauffe text, EquNatureSignal text, EquNom text, EquChauffageAutre text, EquAccesHandisVestiaire text, EquAccueilAucun text, EquipementTirPlateau text, EquipementTir50 text, EquAthNBMarteauMixte text, EquUtilIndividuel text, ComInsee text, EquConfortBainBouillonant text, EquNatNbP10 text, EquOuvertSaison text, EquNatProfMax text, EquNatureAcPubPed text, EquTableauFixe text, InsNom text, EquGestionDSP text, EquNbVestiaireSpo text, EquNatureSKTotalRemontee text, EquTravauxRealDegradation text, EquAthNbCouloirLigne text, EquAccueilDopage text, EquAccesHandimAire text, EquChrono text, GestionTypeGestionnairePrincLib text, EquUtilFormation text, EquNatureAcSecPed text, EquSaeNbCouloir text, EquNatProfMini text, EquAthDev text, EquSaeHauteur text, EquAccueilBureau text, EquAthNbJavelot text, InsNumeroInstall text, EquAnneeService text, EquAthNbSautPerche text, EquNatCouloir text, EquipementTir300 text, EquAccesHandimAucun text, EquNatureAcSecRout text, EquipementTir200 text, EquGpsX text, EquNomBatiment text, EquipementTir100 text, EquGpsY text, EquLargeurEvolution text, EquChauffageNon text, GestionTypeGestionnaireSecLib text, EquAthNbSautHauteur text, EquDateDernierTravauxReal text, EquipementId text, EquUtilScolaire text, EquNatureAutorise text, EquSanitairePublic text, EquAccueilInfirmerie text, EquAccueilClub text, EquChauffageSolaire text, EquAthNbSautTriple text, EquNatNbTTotal text, EquProximite text, EquipNatureSituationLib text, EquChauffageFuel text, EquipementTypeLib text, EquDateDernierTravauxAucun text, EquErpREF text, EquipementTir25 text, EquAthNbDisque text, EquAmenagementAucun text, AnneeTravauxRealLibelle text, EquAccesHandimSaniSpo text, EquNbCouloirPiste text, EquChauffageElectricite text, EquNatNbP3 text, EquNatureClassFedeMaxi text, EquAccesHandimTribune text, FamilleFicheLib text, EquNatNbPTotal text, EquTravauxRealNorme text, EquErpCTS text, EquAthRiviere text, EquAccesHandisTribune text, EquipementFiche text, NatureSolLib text, EquNatSurfacePlageBassin text, EquNatureESTour text, EquipementTir10 text, ComLib text, EquAccueilMedic text, AnneeServiceLib text, EquNatAutre text, EquNaturePDESI text, EquNatRiviere text, EquNatureAlert text, EquNatNbP7 text, EquNatureAcPubMec text, EquNatNbP5 text, EquNatLargeurBassin text, EquErpSG text, EquNatureClassFedeMini text, EquAccueilLocalRangement text, EquNatureAcPubNau text, EquConfortSauna text, EquLongueurEvolution text, EquAccesHandisSaniSpo text, EquNbPlaceTribune text, EquConfortBainVapeur text, EquAthNbSautTotal text, EquNatureAcSecNau text, EquTravauxRealUsager text, EquNbEquIdentique text, EquUtilRecreation text, EquAthNbPoids text, EquNatFM text, EquAccueilSalle text, EquNatImHandi text, EquNatMaV text, EquNatureAcSecMec text, EquAthNbCouloirHorsLigne text, EquipementTirAutre text, EquDemarcheHQE text, EquTravauxRealConformite text, EquNatureAETreuil text, EquNbVestiaireArbitre text, EquAthNbSautLongueur text, EquAthNbLancerTotal text, EquNatureSEVoies text, EquAccesHandisSaniPub text, EquErpRPE text, EquNatMM text, EquAthLongLigneDroite text, EquErpX text, EquConfortAucun text, EquErpR text, EquChauffageGaz text, EquErpO text, EquSaeSurface text, EquErpN text, EquPresencePataugeoir text, EquNatPentaglisse text, EquUtilPerformance text, EquNatureLocTec text, EquErpP text, EquAccesHandimSaniPub text, EquUtilClub text, EquAthNbMarteau text, EquErpL text)''')

conn.commit()
conn.close()

conn = sqlite3.connect('lepythonenbd.db')

c = conn.cursor()

for inst in datainstall["data"]:
	values = [inst["InsLibelleVoie"], inst["InsTransportTrain"], inst["Nb_Equipements"], inst["InsPartLibelle"], inst["InsNbPlaceParkingHandi"], inst["InsNbPlaceParking"], inst["InsTransportBateau"], inst["InsNoVoie"], inst["InsLieuDit"], inst["InsTransportTram"], inst["InsEmpriseFonciere"], inst["Latitude"], inst["ComLib"], inst["InsTransportBus"], inst["InsCodePostal"], inst["InsMultiCommune"], inst["ComInsee"], inst["InsDateMaj"], inst["InsAccessibiliteAucun"], inst["Nb_FicheEquipement"], inst["InsTransportAutre"], inst["InsAccessibiliteHandiSens"], inst["InsGardiennee"], inst["InsTransportMetro"], inst["InsAccessibiliteHandiMoteur"], inst["InsNumeroInstall"], inst["Longitude"]]
	c.execute('''INSERT INTO installation VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', values)


for act in dataact["data"]:
	values = [act["ActCode"], act["EquNbEquIdentique"], act["EquActivitePratique"], act["EquActiviteSalleSpe"], act["ComInsee"], act["ActNivLib"], act["EquipementId"], act["ActLib"], act["EquActivitePraticable"], act["ComLib"]]
	c.execute('''INSERT INTO activite VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', values)

for equip in dataequip["data"]:
	values = [equip["EquSanitaireSportif"], equip["EquErpPA"], equip["EquEclairage"], equip["EquHauteurEvolution"], equip["EquNatSurfaceBassin"], equip["EquNatureAcPubRout"], equip["EquSurfaceEvolution"], equip["EquNatLongueurBassin"], equip["EquSono"], equip["GestionTypeProprietaireSecLib"], equip["EquConfortSolarium"], equip["EquNatTobog"], equip["EquNatNbT1"], equip["EquUtilAutre"], equip["EquTravauxRealVetuste"], equip["EquNatNbT3"], equip["EquNatSurv"], equip["EquConfortAutre"], equip["EquNatSonorisationSub"], equip["EquErpCategorie"], equip["EquAccesHandisAire"], equip["EquAccueilReception"], equip["EquAccueilBuvette"], equip["GestionTypeProprietairePrincLib"], equip["NatureLibelle"], equip["EquDateMaj"], equip["EquAccueilAutre"], equip["EquHauteurSurfaceEvo"], equip["EquNatFormeLib"], equip["EquAccesHandisAucun"], equip["EquErpOA"], equip["EquDouche"], equip["EquAccesHandimVestiaire"], equip["EquNatEclSub"], equip["EquNatureLocPed"], equip["EquVestiaireSpoChauffe"], equip["EquNatureSignal"], equip["EquNom"], equip["EquChauffageAutre"], equip["EquAccesHandisVestiaire"], equip["EquAccueilAucun"], equip["EquipementTirPlateau"], equip["EquipementTir50"], equip["EquAthNBMarteauMixte"], equip["EquUtilIndividuel"], equip["ComInsee"], equip["EquConfortBainBouillonant"], equip["EquNatNbP10"], equip["EquOuvertSaison"], equip["EquNatProfMax"], equip["EquNatureAcPubPed"], equip["EquTableauFixe"], equip["InsNom"], equip["EquGestionDSP"], equip["EquNbVestiaireSpo"], equip["EquNatureSKTotalRemontee"], equip["EquTravauxRealDegradation"], equip["EquAthNbCouloirLigne"], equip["EquAccueilDopage"], equip["EquAccesHandimAire"], equip["EquChrono"], equip["GestionTypeGestionnairePrincLib"], equip["EquUtilFormation"], equip["EquNatureAcSecPed"], equip["EquSaeNbCouloir"], equip["EquNatProfMini"], equip["EquAthDev"], equip["EquSaeHauteur"], equip["EquAccueilBureau"], equip["EquAthNbJavelot"], equip["InsNumeroInstall"], equip["EquAnneeService"], equip["EquAthNbSautPerche"], equip["EquNatCouloir"], equip["EquipementTir300"], equip["EquAccesHandimAucun"], equip["EquNatureAcSecRout"], equip["EquipementTir200"], equip["EquGpsX"], equip["EquNomBatiment"], equip["EquipementTir100"], equip["EquGpsY"], equip["EquLargeurEvolution"], equip["EquChauffageNon"], equip["GestionTypeGestionnaireSecLib"], equip["EquAthNbSautHauteur"], equip["EquDateDernierTravauxReal"], equip["EquipementId"], equip["EquUtilScolaire"], equip["EquNatureAutorise"], equip["EquSanitairePublic"], equip["EquAccueilInfirmerie"], equip["EquAccueilClub"], equip["EquChauffageSolaire"], equip["EquAthNbSautTriple"], equip["EquNatNbTTotal"], equip["EquProximite"], equip["EquipNatureSituationLib"], equip["EquChauffageFuel"], equip["EquipementTypeLib"], equip["EquDateDernierTravauxAucun"], equip["EquErpREF"], equip["EquipementTir25"], equip["EquAthNbDisque"], equip["EquAmenagementAucun"], equip["AnneeTravauxRealLibelle"], equip["EquAccesHandimSaniSpo"], equip["EquNbCouloirPiste"], equip["EquChauffageElectricite"], equip["EquNatNbP3"], equip["EquNatureClassFedeMaxi"], equip["EquAccesHandimTribune"], equip["FamilleFicheLib"], equip["EquNatNbPTotal"], equip["EquTravauxRealNorme"], equip["EquErpCTS"], equip["EquAthRiviere"], equip["EquAccesHandisTribune"], equip["EquipementFiche"], equip["NatureSolLib"], equip["EquNatSurfacePlageBassin"], equip["EquNatureESTour"], equip["EquipementTir10"], equip["ComLib"], equip["EquAccueilMedic"], equip["AnneeServiceLib"], equip["EquNatAutre"], equip["EquNaturePDESI"], equip["EquNatRiviere"], equip["EquNatureAlert"], equip["EquNatNbP7"], equip["EquNatureAcPubMec"], equip["EquNatNbP5"], equip["EquNatLargeurBassin"], equip["EquErpSG"], equip["EquNatureClassFedeMini"], equip["EquAccueilLocalRangement"], equip["EquNatureAcPubNau"], equip["EquConfortSauna"], equip["EquLongueurEvolution"], equip["EquAccesHandisSaniSpo"], equip["EquNbPlaceTribune"], equip["EquConfortBainVapeur"], equip["EquAthNbSautTotal"], equip["EquNatureAcSecNau"], equip["EquTravauxRealUsager"], equip["EquNbEquIdentique"], equip["EquUtilRecreation"], equip["EquAthNbPoids"], equip["EquNatFM"], equip["EquAccueilSalle"], equip["EquNatImHandi"], equip["EquNatMaV"], equip["EquNatureAcSecMec"], equip["EquAthNbCouloirHorsLigne"], equip["EquipementTirAutre"], equip["EquDemarcheHQE"], equip["EquTravauxRealConformite"], equip["EquNatureAETreuil"], equip["EquNbVestiaireArbitre"], equip["EquAthNbSautLongueur"], equip["EquAthNbLancerTotal"], equip["EquNatureSEVoies"], equip["EquAccesHandisSaniPub"], equip["EquErpRPE"], equip["EquNatMM"], equip["EquAthLongLigneDroite"], equip["EquErpX"], equip["EquConfortAucun"], equip["EquErpR"], equip["EquChauffageGaz"], equip["EquErpO"], equip["EquSaeSurface"], equip["EquErpN"], equip["EquPresencePataugeoir"], equip["EquNatPentaglisse"], equip["EquUtilPerformance"], equip["EquNatureLocTec"], equip["EquErpP"], equip["EquAccesHandimSaniPub"], equip["EquUtilClub"], equip["EquAthNbMarteau"], equip["EquErpL"]]
	c.execute('''INSERT INTO equipement VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''', values)

conn.commit()

#for row in c.execute('SELECT * FROM installation ORDER BY nom'):
#    print(row)

for row in c.execute('SELECT * FROM activite'):
    print(row)

conn.close()
