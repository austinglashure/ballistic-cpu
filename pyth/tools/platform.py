import math


class Platform():
    def __init__(self, bc, cal_inches, muzzle_vel_ft, grains):
        self.bc = bc
        self.cal_inches = cal_inches
        self.muzzle_vel_ft = muzzle_vel_ft
        self.grains = grains
        # SI unit mass conversion
        self.mass = self.grains / 15432
        # SI unit velocity conversion
        self.muzzle_vel = muzzle_vel_ft / 3.2808398950131
        # SI unit caliber conversion
        self.caliber = self.cal_inches * 0.0254

    def calculateCrossSectionalArea(self):
        radius = self.caliber / 2
        self.cross_sectional_area = math.pi * pow(radius, 2)
    
    def calculateDragCoefficient(self, air_density):
        self.calculateCrossSectionalArea()
        self.drag_coef = (0.5 * air_density * self.bc *
                          self.cross_sectional_area)

    def show(self):
        print(f"Muzzle vel: {self.muzzle_vel_ft} ft/sec")
        print(f"BC: {self.bc}")
        print(f"Caliber: {self.cal_inches} and Grains: {self.grains}")