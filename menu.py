#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
# import time


def pedido():
    pedido= Toplevel(menu)
    pedido.resizable(0,0) 
    pedido.geometry('1024x900') 

    # pedido.focus_set()
    # pedido.grab_set()
    # pedido.wait_window(pedido)
    scroll = Scrollbar( orient = VERTICAL)
    
    # scroll.config(command=listbox.yview)
    scroll.pack(side = RIGHT, fill = Y)

    listbox = Listbox(pedido,width = 20, height = 20, yscrollcommand = scroll.set)
    # listbox.grid(column=0,row=0)
    scroll.config(command=listbox.yview)
    # scroll.grid(column=1, row=0, sticky='NS')
    # scroll.pack(side = RIGHT, fill = Y)
    
   
    listbox.insert(END, 'A list entry',)

    for item in ['one','two','three','four','one','two','three','four','one','two','three','four','one','two','three','four','one','two','three','four','one','two','three','four','one','two','three','four','one','two','three','four','one','two','three','four']:
            listbox.insert(END,item)

    listbox.place(relx = 0.1,rely = 0.1)





def menu():
    global menu
    menu = Tk()
    menu.title("BitApp") 
    menu.resizable(0,0) 
    menu.geometry('1024x900') 


    frame = Frame(menu, width=1024, height=900)

    boton1 = Button(frame, text="Pedido",width=30,height = 2, command = pedido)
    boton1.place(relx=0.5, rely=0.3, anchor=CENTER)

    boton2 = Button(frame, text="Contraindicaciones",width=30,height = 2)
    boton2.place(relx=0.5, rely=0.4, anchor=CENTER)

    boton3 = Button(frame, text="Dosis",width=30,height = 2)
    boton3.place(relx=0.5, rely=0.5, anchor=CENTER)

    boton4 = Button(frame, text="Historial",width=30,height = 2)
    boton4.place(relx=0.5, rely=0.6, anchor=CENTER)

    boton5 = Button(frame, text="Vencimientos",width=30,height = 2)
    boton5.place(relx=0.5, rely=0.7, anchor=CENTER)



    frame.pack(side="top", anchor="w") #Empaqueta el elemento en la raíz si no, no se puede mostrar, paramestros para posición

#Loop principal
# root.mainloop() #ciclo para que inicien los procesos y capte los eventos
