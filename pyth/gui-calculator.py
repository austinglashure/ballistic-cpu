from cgitb import text
import balls # imports everything in that folder
import tkinter as tk

# triggered when calculate button is pressed
def on_calculate_press():
    global target_range
    val = target_range.get()
    print("You pressed the \"Calculate\" button")
    print(f"Target Range: {val}")

window = tk.Tk()
# style the window
window.title("Ballistic CPU")
window.geometry("500x700")  # widthxheight sets window size
# range entry creation
range_label = tk.Label(window, text="Range")
range_label.pack()
target_range = tk.Entry(window,
                        text="range")                      
target_range.pack()
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
    