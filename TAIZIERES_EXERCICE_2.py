# exercice2.py
from CLASSE_ROBOT import Robot  

class Humain:
    def __init__(self, nom, sexe):
        self.__nom = nom
        self.__sexe = sexe
        self.aliments = []

    def setNom(self, x):
        self.__nom = x

    def getNom(self):
        return self.__nom
    
    def setSexe(self, x):
        self.__sexe = x

    def getSexe(self):
        return self.__sexe
    
    def mangerAliment(self, aliment):
        self.aliments.append(aliment)
        print(self.__nom, "vient d'ingérer l'aliment :", aliment)
        print("L'estomac de", self.__nom, "contient", self.aliments)

    def digererAliment(self):
        if len(self.aliments) != 0:
            self.aliments.clear()
            print("L'estomac de", self.__nom, "est vide")
        else:
            print("L'estomac de", self.__nom, "est déjà vide")

class Cyborg(Robot, Humain):
    def __init__(self, nom, sexe):
        Robot.__init__(self, nom)
        Humain.__init__(self, nom, sexe)

    def cyborgSurpuissant(self):  
        print(self.getNom(), "mange des humains")
    

if __name__ == "__main__":
    cyborg1 = Cyborg("r2D2", "Homme")
    cyborg1.mangerAliment("poire")
    cyborg1.mangerAliment("viande")
    cyborg1.mangerAliment("fraise")
    cyborg1.mangerAliment("vanille")
    cyborg1.digererAliment()
    cyborg1.cyborgSurpuissant()
