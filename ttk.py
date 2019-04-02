from tkinter import *
from tkinter import ttk
def main():
    root = Tk()
    root.mainloop()
    month=StringVar()
    combobox = ttk.Combobox(root,textvariable = month)
    combobox.pack()

main()
