TIME_IMPULSE = 0.01


class Flight():
    def __init__(self, meters_secs, drag_coefficient, range, bullet_mass):
        self.vel0 = meters_secs
        self.drag_coef = drag_coefficient
        self.range = range
        self.mass = bullet_mass

    def calculateInstantaneousForce(self):
        self.instant_drag_force = self.drag_coef * self.vel0 * self.vel0  # pow(self.vel0, 2)

    def calculateInstantDeceleration(self):
        self.calculateInstantaneousForce()
        self.instant_decel = -1 * (self.instant_drag_force / self.mass)
    
    def calculateVelocityFinal(self):
        self.calculateInstantDeceleration()
        self.vel_final = self.vel0 + (self.instant_decel * TIME_IMPULSE)
    
    def calculateDisplacement(self):
        self.calculateVelocityFinal()
        avg = (self.vel0 + self.vel_final) / 2.0
        self.displacement = avg * TIME_IMPULSE
    
    def calculateFlightTime(self):
        foo = 0.0
        self.flight_time = 0.0
        while foo < self.range:
            self.calculateDisplacement()
            foo += self.displacement
            self.flight_time += TIME_IMPULSE
            self.vel0 = self.vel_final
            
    def calculateBulletDrop(self):
        self.calculateFlightTime()
        self.bullet_drop = -4.9 * pow(self.flight_time, 2)
