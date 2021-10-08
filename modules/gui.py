import tkinter as tk
import tkinter.ttk as ttk

SELECTION = {}

def rendergui():
    window = tk.Tk()
    window.geometry('500x300')
    options = ['a', 'b', 'c', 'd', 'e']

    selected = tk.StringVar(value='select')
    global cbox
    cbox = ttk.Combobox(window, textvariable=selected)
    cbox['values'] = options
    cbox['state'] = 'readonly'
    cbox.pack(fill='x', padx=5, pady=5)
    cbox.bind('<<ComboboxSelected>>', cbox_changed)

    window.mainloop()

def cbox_changed(event):
    print(cbox.get())