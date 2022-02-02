from cgitb import text
import balls # imports everything in that folder
import tkinter as tk
'''
WEATHER
Temp, pressure, humidity
WEAPON SYSTEM
ballistic coefficient, caliber, bullet mass, muzzle velocity
BALLISTIC FACTORS
will be range for now, but soon
    shooter position
    target position
'''

# triggered when calculate button is pressed
def on_calculate_press():
    global target_range
    global temperature_value, press_value, hum_value
    range_val = target_range.get()
    temp_val = temperature_value.get()
    hum_val = hum_value.get()
    press_val = press_value.get()
    print("You pressed the \"Calculate\" button")
    print(f"Target Range: {range_val}")
    print(f"Range Temperature: {temp_val}")
    print(f"Humidity: {hum_val}")
    print(f"Pressure: {press_val}")


window = tk.Tk()
# style the window
window.title("Ballistic CPU")
window.geometry("500x700")  # widthxheight sets window size
# range entry creation
range_label = tk.Label(window, text="Range")
range_label.pack()
target_range = tk.Entry(window)                      
target_range.pack()
# temperature
temperature_label = tk.Label(window, text="Temperature")
temperature_label.pack()
temperature_value = tk.Entry(window)
temperature_value.pack()
# humidity
hum_label = tk.Label(window, text="Humidity")
hum_label.pack()
hum_value = tk.Entry(window)
hum_value.pack()
# pressure
press_label = tk.Label(window, text="Pressure")
press_label.pack()
press_value = tk.Entry(window)
press_value.pack()
# calculate button creation
calculate_button = tk.Button(window,
                             text="Calculate",
                             bg="red",
                             fg="white",
                             width=50,
                             height=2,
                             command=on_calculate_press)
calculate_button.pack()

window.mainloop()
    