import pandas as pd
import numpy as np
import openpyxl as pyxl
from tools import weather, platform, ballistics

rig = platform.Platform(.45, .308, 2821, 165)
rig.show()