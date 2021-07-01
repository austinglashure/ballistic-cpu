from tools import weather as w
from tools import platform as p
from tools import ballistics as b

# .308 weapon profile
bc, cal, muzz_vel, grains = 0.45, 0.308, 2821.5, 165
a = p.Platform(bc, cal, muzz_vel, grains)

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
    a.calculateDragCoefficient(conditions.air_density)
    # present data and see if user wants to reinput data
    print(  "\nTemperature: {} degrees Fahrenheit".format(fahr),
            "\nPressure: {} inches of Mercury".format(inHg),
            "\nHumidity: {}%".format(hum))
    reset = int(input("Are you happy with these settings?\n(1/0): "))
    # conditional test to break the loop
    if reset == 1:
       picking_weather = False

print("Weapon: {} grain {} with a bc ".format(a.grains, a.cal_inches),
        "of {} and a muzzle velocity of {}\n".format(a.bc, round(a.muzzle_vel)),
        "meters per second")
# range and shot calculation loop
shooting = True
while shooting:
    range = int(input("\nWhat is the range? (m): "))
    shot = b.Flight(a.muzzle_vel, a.drag_coef, range, a.mass)
    shot.calculateBulletDrop()
    print(str(shot.bullet_drop) + " meters vertical adjustment\n")
    again = int(input("Would you like to input another range?\n(1/0): "))
    if again == 0:
        shooting = False
