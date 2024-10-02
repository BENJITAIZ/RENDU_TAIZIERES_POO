import time

class Robot: 
    def __init__(self, nom="<nom>"):
        self.__nom = nom
        self.__alimentation = False
        self.__vitesse_actuelle = 0
        self.__niveau_batterie = 0  # Pourcentage de batterie (0-100)
        self.__recharge = False

    def allumer(self):
        if not self.__alimentation:
            self.__alimentation = True
            print(f"{self.__nom} est maintenant ((allumé)).")
        else:
            print(f"{self.__nom} est déjà ((allumé)).")

    def eteindre(self):
        if self.__alimentation:
            self.__alimentation = False
            self.__vitesse_actuelle = 0  # Arrête le robot s'il est éteint
            print(f"{self.__nom} est maintenant ((éteint)).")
        else:
            print(f"{self.__nom} est déjà ((éteint)).")

    def recharger_batterie(self):
        if self.__alimentation:
            print(f"Recharge de la batterie de {self.__nom}... (Temps d'attente 10 secondes)")
            for i in range(10):
                time.sleep(1)  # Simule le temps de charge
                self.__niveau_batterie += 10  # Charge 10% par seconde
                if self.__niveau_batterie > 100:
                    self.__niveau_batterie = 100
                print(f"Niveau de batterie de {self.__nom} est de  : {self.__niveau_batterie}%")
        else:
            print(f"{self.__nom} est en charge (quand il est ÉTEINT)...")
            for i in range(10):
                time.sleep(1)  # Simule le temps de charge
                self.__niveau_batterie += 10  # Charge 10% par seconde
                if self.__niveau_batterie > 100:
                    self.__niveau_batterie = 100
                print(f"Niveau de batterie : {self.__niveau_batterie}%")

    def definir_vitesse(self, vitesse):
        if self.__alimentation and self.__niveau_batterie > 0:
            self.__vitesse_actuelle = vitesse
            print(f"{self.__nom} se déplace à {self.__vitesse_actuelle} m/s.")
        else:
            print(f"{self.__nom} ne peut pas se déplacer. Alimentation : {self.__alimentation}, Niveau de Batterie : {self.__niveau_batterie}%")

    def obtenir_vitesse(self):
        return self.__vitesse_actuelle

    def arreter_deplacer(self):
        if self.__alimentation:
            self.__vitesse_actuelle = 0
            print(f"{self.__nom} a arrêté de se déplacer.")
        else:
            print(f"{self.__nom} est ÉTEINT et ne peut pas se déplacer.")

    def obtenir_resume(self):
        etat = "((allumé))" if self.__alimentation else "((éteint))"
        print(f"Nom du Robot : {self.__nom}")
        print(f"État d'Alimentation : {etat}")
        print(f"Niveau de Batterie : {self.__niveau_batterie}%")
        print(f"Vitesse Actuelle : {self.__vitesse_actuelle} m/s")

# Test
robot = Robot("Robocop")
robot.allumer()
robot.recharger_batterie()
robot.definir_vitesse(5)
robot.obtenir_resume()
robot.arreter_deplacer()
robot.eteindre()
