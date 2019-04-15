import tkinter as tk

root = tk.Tk()


root.title("BitApp") 
root.resizable(0,0) 

root.geometry('1024x900') 


frame = tk.Frame(root, width=1024, height=900)

boton = tk.Button(frame, text="Pedido",width=30,height = 2)
boton.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
# boton.pack()
boton2 = tk.Button(frame, text="Contraindicaciones",width=30,height = 2)
boton2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

boton3 = tk.Button(frame, text="Dosis",width=30,height = 2)
boton3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

boton3 = tk.Button(frame, text="Historial",width=30,height = 2)
boton3.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

boton3 = tk.Button(frame, text="Vencimientos",width=30,height = 2)
boton3.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

frame.pack(side="top", anchor="w") #Empaqueta el elemento en la raíz si no, no se puede mostrar, paramestros para posición

#Loop principal
root.mainloop() #ciclo para que inicien los procesos y capte los eventos