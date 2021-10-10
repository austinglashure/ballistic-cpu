'''
Temperature range: -65F - 130F
Humidity: 0-100
Pressure: 250 Torr to 815 Torr

Caliber: .177 to .950
Ballistic Coefficient: 
0.1 to 1
'''

import pandas as pd
import numpy as np
import openpyxl as pyxl
from tools import weather, platform, ballistics

hum_s = np.array(range(0, 101))
temp_s = np.array(range(-65, 131))  # in fahrenheit
presh_s = np.linspace(10, 30, 50)  # in inHg
range_s = np.linspace(100, 2000, 50)  # in meters

gun = platform.Platform(.45, .308, 2821, 165)



data = []
for hum in hum_s:
    for temp in temp_s:
        for pres in presh_s:
            for range in range_s:
                weather_prof = weather.Weather(temp, pres, hum)
                air_density = weather_prof.air_density
                drag_coef = gun.calculateDragCoefficient(air_density)
                shot = ballistics.Flight(gun.muzzle_vel, gun.bc, range, gun.mass)
                shot.calculateBulletDrop()
                flight_time = shot.flight_time
                bullet_drop = shot.bullet_drop
                data_point = {  'range': range,
                                'temp': temp,
                                'pressure': pres,
                                'humidity': hum,
                                'flight time': flight_time,
                                'bullet drop': bullet_drop
                            }
                data.append(data_point)
                if len(data) % 1000 == 0:
                    print(len(data))

set = pd.DataFrame(data)
print(set.head())
