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
import tools

hum_s = np.array(range(0, 101))
temp_s = np.array(range(-65, 131))  # in fahrenheit
presh_s = np.linspace(10, 30, 50)  # in inHg
