import pandas as pd
import numpy as np
import openpyxl as pyxl
from tools import weather, platform, ballistics

rig = platform.Platform(.45, .308, 2821, 165)
rig.show()

def calculate_data(temp, hum, inhg, range):
    w = weather.Weather(temp, inhg, hum)
    rig.calculateDragCoefficient(w.air_density)
    b = ballistics.Flight(rig.muzzle_vel, rig.bc, range, rig.mass)
    b.calculateBulletDrop()
    data = {
            "temp": temp,
            "humidity": hum,
            "pressure": inhg,
            "flight time": b.flight_time,
            "bullet drop": b.bullet_drop
            }
    return data

pressures = np.linspace(10, 35, 3)
humidities = np.linspace(0, 100, 4)
temperatures = np.linspace(-55, 130, 5)
ranges = np.linspace(150, 2500, 5)
dataset = []
for p in pressures:
    for h in humidities:
        for t in temperatures:
            for r in ranges:
                print("here")
                data = calculate_data(t, h, p, r)
                print(data)
                dataset.append(data)
