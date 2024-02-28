

def edades():
    edad=int(input("escriba su edad: "))
    print("eres Elegible")if edad>17 and edad<66 else print("no eres elegible")
    
def clave():

    usua= input()
    usua=True if usua=="usuario123"else False
    contra=input()
    contra=True if contra=="456"else False
    print("usuario correcto")if usua and contra==True else print("usuario o contraseña incorrecto")
def edades():
    edad1=input()
    edad2=input()
    if edad2==edad1:
        print("iguales")
    else:
        print("edad 1 mayor") if edad1>edad2 else print("edad2 mayor")

from tkinter import *
root = Tk()
root.mainloop()


