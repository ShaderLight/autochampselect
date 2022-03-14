import logging

import tkinter as tk
import tkinter.ttk as ttk

from cv2 import log

from .input import pre_match_loop, selectchamp, getlolwindow
from .getdata import get_champ_list

SELECTION = {}

def rendergui():
    global window

    window = tk.Tk()
    window.geometry('500x300')
    window.title('AutoChampSelect')
    options = get_champ_list()

    picktext = tk.StringVar(value='Pick')
    bantext = tk.StringVar(value='Ban')
    
    global pickbox
    global banbox
    global bancheck
    global start_btn

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

    global with_ban_phase
    with_ban_phase = tk.BooleanVar()
    with_ban_phase.set(1)
    bancheck = tk.Checkbutton(window, text="Ban phase?", variable=with_ban_phase, offvalue=False, onvalue=True, command=bancheck_changed)
    bancheck.pack(fill='x', padx=5, pady=5)
    bancheck.select()
    bancheck.pack()

    start_btn = tk.Button(window, text='Start', command=start)
    start_btn.pack(fill='x', padx=5, pady=5)

    quit_btn = tk.Button(window, text='Quit', command=quit)
    quit_btn.pack(fill='x', padx=5, pady=5)
    
    window.mainloop()


def pickbox_changed(event):
    logging.debug('Pickbox: {}'.format(pickbox.get()))
    SELECTION['pick'] = pickbox.get()


def banbox_changed(event):
    logging.debug('Banbox: {}'.format(banbox.get()))
    SELECTION['ban'] = banbox.get()


def bancheck_changed():
    logging.debug('Bancheck pressed, value: {}'.format(with_ban_phase.get()))
    if not with_ban_phase.get():
        banbox.configure(state='disabled')
        logging.debug('Banbox disabled')
    else:
        banbox.configure(state='enabled')
        logging.debug('Banbox enabled')


def start():
    banbox.configure(state='disabled')
    pickbox.configure(state='disabled')
    bancheck.configure(state='disabled')
    start_btn.configure(state='disabled')
    return pre_match_loop(window, with_ban_phase.get(), SELECTION)


def quit():
    logging.debug('Quitting...')
    window.destroy()
    raise KeyboardInterrupt