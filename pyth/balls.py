import math
"""
                Basic Thrust of this!
1. Make GUI to dynamically show bullet drop
2. Graph it as well

"""
mass_molar_air = 0.0289654  # kg/mol
mass_molar_vapor = 0.018016  # kg/mol
constant_gas_universal = 8.312  # J/(K*mol)
class Air:
    def __init__(self, temperature, pressure, humidity):
        self.farenheit = temperature
        self.inHg = pressure
        self.humidity = humidity
    # Ancillary Calculations and conversions
        self.pressure = self.inHg / 0.00029530  # in Pa
        self.celcius = (self.farenheit - 32) / 1.8
        self.kelvin = self.celcius + 273.15

    def saturation_vapor_pressure(self):
        exp = 7.5 * self.celcius / (self.celcius + 237.3)
        self.saturation_vapor_pressure = 6.1078 * 100 * math.pow(10, exp)  # the *100 is to set the value from hPa to Pa

    def partial_pressure(self):
        self.vapor_pressure = self.saturation_vapor_pressure * self.humidity
        self.dry_pressure = self.pressure - self.vapor_pressure

    def air_density(self):
        self.saturation_vapor_pressure()
        self.partial_pressure()
        self.air_density = (self.dry_pressure * mass_molar_air + self.vapor_pressure * mass_molar_vapor) / (constant_gas_universal * self.kelvin)


class Gun:
    time_impulse = 0.001
    def __init__(self, BC, caliber, muzzle_vel, grains):
        self.ball_coef = BC
        self.caliber = caliber
        self.muzzle_vel = muzzle_vel / 3.2808398950131  # m/s
        self.mass = grains / 15432  # kg
        self.cross_sectional_area()
        self.vel0 = muzzle_vel
        self.flight_time = 0

    def cross_sectional_area(self):
        radius = self.caliber * 0.0254 / 2  # in m
        pi = 3.1415926
        self.cross_sectional_area = pi * pow(radius, 2)

    def get_coef(self, air_density):
        self.coef = .5 * air_density * self.ball_coef * self.cross_sectional_area
        print("coef {}".format(self.coef))
    def get_inst_force(self):
        self.inst_force = self.coef * self.vel0 * self.vel0
        print("force {}".format(self.inst_force))

    def get_inst_acc(self):
        self.instant_acc = -self.inst_force / self.mass
        print("inst accel {}".format(self.instant_acc))

    def get_post_vel(self):
        decel = self.instant_acc * self.time_impulse
        print("vel0: {}".format(self.vel0))
        self.post_vel = self.vel0 + decel
        print("velf: {}".format(self.post_vel))

    def get_displacement(self):
        avg = (self.vel0 + self.post_vel) / 2
        self.displacement = avg * self.time_impulse

    def get_flight_time(self, distance):
        self.flight_time = 0
        while distance > 0:
            self.get_inst_force()

            self.get_inst_acc()
            self.get_post_vel()
            self.get_displacement()
            distance -= self.displacement
            self.flight_time += self.time_impulse
            self.vel0 = self.post_vel
        vel0 = self.muzzle_vel
    
    def bullet_drop(self):
        self.bullet_drop = -4.9 * self.flight_time * self.flight_time
