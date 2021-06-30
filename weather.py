# gas constants
AIR_MOLAR_MASS = 0.0289654  # kg/mol
VAPOR_MOLAR_MASS = 0.018016  # kg/mol
UNIVERSAL_GAS_CONSTANT = 8.312  # J/(K*mol)

# line limit ---------------------------------------------------------------->
class Weather:
    def __init__(self, fahrenheit, inHg, humidity):
        self.fahrenheit = fahrenheit
        self.inHg = inHg
        self.humidity = humidity
        # SI pressure conversion
        self.pascals = self.inHg * 3386.38867
        # SI and Kelvin temperature conversion
        self.celcius = (self.fahrenheit - 32) / 1.8
        self.kelvin = self.celcius + 273.15
        self.calculateAirDensity()
        
    def calculateSaturationVaporPressure(self):
        exponent = 7.5 * self.celcius / (self.celcius + 237.3)
        self.saturation_pressure = 6.1078 * 100 * pow(10, exponent)

    def calculatePartialPressures(self):
        self.calculateSaturationVaporPressure()
        self.vapor_pressure = self.saturation_pressure * self.humidity/100
        self.dry_pressure = self.pascals - self.vapor_pressure

    def calculateAirDensity(self):
        self.calculatePartialPressures()
        self.air_density = ((self.dry_pressure * AIR_MOLAR_MASS +
                            self.vapor_pressure * VAPOR_MOLAR_MASS)/
                            (UNIVERSAL_GAS_CONSTANT * self.kelvin))
