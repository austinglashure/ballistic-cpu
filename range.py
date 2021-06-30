import weather as w
import platform as p
import ballistics as b

fahr, inHg, hum = 85, 30, 100
conditions = w.Weather(fahr, inHg, hum)
# .308 weapon profile
bc, cal, muzz_vel, grains = 0.45, 0.308, 2821.5, 165
mine = p.Platform(bc, cal, muzz_vel, grains)
mine.calculateDragCoefficient(conditions.air_density)
print(mine.drag_coef)

shot = b.Flight(mine.muzzle_vel, mine.drag_coef, 500, mine.mass)
shot.calculateBulletDrop()
print(shot.bullet_drop)  # -3.05809
print(shot.flight_time)  # 0.79

