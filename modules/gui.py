import logging

import tkinter as tk
import tkinter.ttk as ttk


SELECTION = {}

def rendergui():
    window = tk.Tk()
    window.geometry('500x300')
    options = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    picktext = tk.StringVar(value='Pick')
    bantext = tk.StringVar(value='Ban')
    
    global pickbox
    global banbox

    pickbox = ttk.Combobox(window, textvariable=picktext)
    pickbox['values'] = options
    pickbox['state'] = 'readonly'
    pickbox.pack(fill='x', padx=5, pady=5)
    pickbox.bind('<<ComboboxSelected>>', pickbox_changed)

    banbox = ttk.Combobox(window, textvariable=bantext)
    banbox['values'] = options
    banbox['state'] = 'readonly'
    banbox.pack(fill='x', padx=5, pady=5)
    banbox.bind('<<ComboboxSelected>>', banbox_changed)

    window.mainloop()

def pickbox_changed(event):
    logging.debug('Pickbox: {}'.format(pickbox.get()))
    SELECTION['pick'] = pickbox.get()

def banbox_changed(event):
    logging.debug('Banbox: {}'.format(banbox.get()))
    SELECTION['ban'] = banbox.get()