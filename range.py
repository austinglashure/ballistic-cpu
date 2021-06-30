from tools import weather as w
from tools import platform as p
from tools import ballistics as b


# .308 weapon profile
bc, cal, muzz_vel, grains = 0.45, 0.308, 2821.5, 165
mine = p.Platform(bc, cal, muzz_vel, grains)

# weather loop
picking_weather = True
while picking_weather:
    # query the data
    fahr = int(input("What's the temperature? (fahrenheit)\n"))
    inHg = float(input("What is the air pressure? (inHg)\n"))
    hum = int(input("What is the humidity?\n"))
    # plug it into weather class
    conditions = w.Weather(fahr, inHg, hum)
    # get drag coefficient for ballistics
    mine.calculateDragCoefficient(conditions.air_density)
    # present data and see if user wants to reinput data
    print(  "\nTemperature: {} degrees Fahrenheit".format(fahr),
            "\nPressure: {} inches of Mercury".format(inHg),
            "\nHumidity: {}%".format(hum))
    reset = int(input("Are you happy with these settings?\n(1/0): "))
    # conditional test to break the loop
    if reset == 1:
       picking_weather = False

shot = b.Flight(mine.muzzle_vel, mine.drag_coef, 500, mine.mass)
shot.calculateBulletDrop()
print(shot.bullet_drop)
