import balls # imports everything in that folder
import tkinter as tk

def on_calculate_press():
    print("You pressed the \"Calculate\" button")

window = tk.Tk()
window.title("Ballistic CPU")
title_label = tk.Label(window, text="Go Ballistic!")
title_label.pack()
window.geometry("500x700")  # widthxheight sets window size
calculate_button = tk.Button(window, text="Calculate", bg="red", fg="white", width=50, height=2, command=on_calculate_press)
calculate_button.pack()
window.mainloop()
    