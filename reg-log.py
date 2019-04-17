from tkinter import *
import os


def delete1():
  screen1.destroy()

def delete2(): # con el destroy eliminamos el evento de la pantalla el invocar la misma
  screen3.destroy()

def delete3():
  screen4.destroy()

def delete4():
  screen5.destroy()

def login_sucess():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("Acceso")
  screen3.geometry("250x200")
  Label(screen3, text = "Login Correcto").pack()
  Button(screen3, text = "OK", command =delete2).pack()

def pass_no_reconocido(): # condicion chequea el Pass que no falle para el Log
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("AVISO")
  screen4.geometry("250x200")
  Label(screen4, text = "Error password").pack()
  Button(screen4, text = "Fallo", command =delete3).pack()

def user_no_encontrado(): # Esta condicion chequea los campos de loguin
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("AVISO")
  screen5.geometry("250x200")
  Label(screen5, text = "No existe ese Usuario").pack()
  Button(screen5, text = "Fallo", command =delete4).pack()

  
def registro_user():
  print("working")
  
  username_info = username.get()
  password_info = password.get()

  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registro Exitoso", fg = "green" ,font = ("calibri", 11)).pack()
  


def login_verificar():
  
  username1 = user_verificar.get()
  password1 = pass_virificar.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  list_of_files = os.listdir()  # este es el algoritmo para verificar que no se repita el log
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_sucess()
    else:
        pass_no_reconocido()

  else:
        user_no_encontrado()
  


def registro():  # pantalla de Registro 
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Registro")
  screen1.geometry("300x250")
  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "Por favor detallar Informacion").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Username * ").pack()
 
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Contraseña * ").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Registro", width = 10, height = 1, command = registro_user).pack()

def login():    # Pantalla de logueo 
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("300x250")
  Label(screen2, text = "Please enter details below to login").pack()
  Label(screen2, text = "").pack()

  global user_verificar
  global pass_virificar
  
  user_verificar = StringVar()
  pass_virificar = StringVar()

  global username_entry1
  global password_entry1
  
  Label(screen2, text = "Username * ").pack()
  username_entry1 = Entry(screen2, textvariable = user_verificar)
  username_entry1.pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Password * ").pack()
  password_entry1 = Entry(screen2, textvariable = pass_virificar)
  password_entry1.pack()
  Label(screen2, text = "").pack()
  Button(screen2, text = "Login", width = 10, height = 1, command = login_verificar).pack()
  
  

def main_screen():
  #global screen6
  #screen6 = Toplevel(screen) queda comentado ya que de otra manera crea una ventana nueva
  #screen6.geometry("300x250") la idea es que cargue desde la principal
  #screen6.title("Loguearse")  
  Label(text = "Credenciales", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Login", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Registro",height = "2", width = "30", command = registro).pack()

  #screen.mainloop()

#main_screen()

def First():  # ESTA ES LA PRIMER PANTALLA TENGO UN ERROR CON LA DE LOG
  global screen
  screen = Tk() #  el TK hace que este screen sea el principal de carga 
  screen.geometry("500x350") # Determina las dimensiones de las pantallas 
  screen.title("Inicio")
  Label(text = "Identificarse", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  Button(text = "Usuario", height = "2", width = "30", command = main_screen).pack()
  Label(text = "").pack()
  Button(text = "Administrador",height = "2", width = "30", command = registro).pack()

  screen.mainloop()

First()