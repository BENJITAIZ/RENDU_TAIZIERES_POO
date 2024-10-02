from abc import ABC, abstractmethod

# Classe abstraite représentant un véhicule non habité (Unmanned Vehicle)
class UnmannedVehicle(ABC):
    @abstractmethod
    def execute_mission(self):
        pass

# Classe qui définit le type de mouvement terrestre
class GroundMovement:
    def move_on_ground(self):
        print("Le véhicule se déplace sur le terrain.")

# Classe qui définit le type de mouvement aérien
class AirMovement:
    def move_in_air(self):
        print("Le véhicule se déplace dans l'air.")

# Classe qui définit le type de mouvement sous-marin
class UnderwaterMovement:
    def move_underwater(self):
        print("Le véhicule se déplace sous l'eau.")

# UUV - Unmanned Underwater Vehicle (héritage multiple)
class UUV(UnmannedVehicle, UnderwaterMovement):
    def execute_mission(self):
        print("Le UUV exécute une mission sous-marine.")
        self.move_underwater()

# UAV - Unmanned Aerial Vehicle
class UAV(UnmannedVehicle, AirMovement):
    def execute_mission(self):
        print("Le UAV exécute une mission aérienne.")
        self.move_in_air()

# UGV - Unmanned Ground Vehicle
class UGV(UnmannedVehicle, GroundMovement):
    def execute_mission(self):
        print("Le UGV exécute une mission terrestre.")
        self.move_on_ground()

# Fonction qui accepte n'importe quel UnmannedVehicle (polymorphisme)
def launch_mission(vehicle: UnmannedVehicle):
    vehicle.execute_mission()


uuv = UUV()
uav = UAV()
ugv = UGV()

launch_mission(uuv)
launch_mission(uav)
launch_mission(ugv)
