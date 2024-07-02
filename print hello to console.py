import tkinter as tk
from tkinter import ttk

def print_hello():
    print("Hello!!!")

window= tk.Tk()
window.geometry("200x100")
window.title("Print hello")
#entry
text2= ttk.Entry(master = window)
text2.pack(pady=10)
#label
label2 = ttk.Label(master = window, text ="My label")
label2.pack()
#print hello
btn = ttk.Button(master= window, text= "Print hello", command = print_hello)
btn.pack()
#window loop
window.mainloop()