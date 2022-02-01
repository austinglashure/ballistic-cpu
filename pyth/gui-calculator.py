import balls # imports everything in that folder
import tkinter as tk

# triggered when calculate button is pressed
def on_calculate_press():
    print("You pressed the \"Calculate\" button")

window = tk.Tk()
# style the window
window.title("Ballistic CPU")
window.geometry("500x700")  # widthxheight sets window size
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
    