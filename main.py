import tkinter as tk
from tkinter import Label, Entry, Button
import AUC


window = tk.Tk()
window.title("Area under curve calulator")
window.geometry("640x480")

label1 = Label(window, text="Enter function: ")
label1.pack()
entry1 = Entry(window)
entry1.pack()

label2 = Label(window, text="Enter Limit(a): ")
label2.pack()
entry2 = Entry(window)
entry2.pack()

label3 = Label(window, text="Enter Limit(b): ")
label3.pack()
entry3 = Entry(window)
entry3.pack()

label3 = Label(window, text="Enter iterations(n): ")
label3.pack()
entry4 = Entry(window)
entry4.pack()

def printer(event=None):
  label4.config(text="The area under the curve is {:.3f}".format(AUC.trapezoidal_rule(entry1.get(), float(entry2.get()), float(entry3.get()), int(entry4.get()))))
  

button = Button(text="Calculate", command=printer)
button.pack()
label4 = Label(window, text='')
label4.pack()
tk.mainloop()