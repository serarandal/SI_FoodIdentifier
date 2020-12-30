import ProjectFindFood
from tkinter import *

#------------------IMPORTAR TXT---------------------
def pruebaTexto():
    archivo_texto = open("lista.txt","r")
    texto = archivo_texto.read()
    archivo_texto.close()
    return texto    
    
#------------------Tercera Ventana---------------------
def createListWindow():
    listWindow = Toplevel(window)
    listWindow.title("Lista de Alimentos")
    listWindow.resizable(0,1)
    listWindow.geometry("400x160")
    listFrame = Frame(listWindow)
    listFrame.pack()     
    
    #------------------CABECERA---------------------
    
    listcabecera = Label(listFrame, text = "Lista de Alimentos")
    listcabecera.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 2) 
    
    #------------------CUERPO---------------------
   
    inputTexto = Label(listFrame, text = pruebaTexto())
    inputTexto.grid(row=2,column=1, padx = 10, pady = 10, columnspan = 2)    
    
    boton11 = Button(listFrame, text = "Cerrar", width = 56, height = 2,command = listWindow.destroy)
    boton11.grid(row = 4, column = 1, columnspan = 2)

    
#------------------Segunda Ventana---------------------
def createNewWindow():
    newWindow = Toplevel(window)
    newWindow.title("Alimentos")
    newWindow.resizable(0,0)
    newWindow.geometry("400x160")
    xFrame = Frame(newWindow)
    xFrame.pack()

    #------------------CABECERA---------------------
    
    cabecera = Label(xFrame, text = "Seleccione el alimento que desea escanear")
    cabecera.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 5) 
    
    #------------------PRIMERA FILA------------------
    
    boton1 = Button(xFrame, text = "Berenjenas", width = 10, height = 2, command = lambda:combine_funcs("berenjena"))
    boton1.grid(row = 2, column = 1)
    
    boton2 = Button(xFrame, text = "Fresas", width = 10, height = 2, command = lambda:combine_funcs("fresa"))
    boton2 .grid(row = 2, column = 2)
    
    boton3 = Button(xFrame, text = "Huevos", width = 10, height = 2, command = lambda:combine_funcs("huevo"))
    boton3.grid(row = 2, column = 3)
    
    boton4 = Button(xFrame, text = "Leche", width = 10, height = 2, command = lambda:combine_funcs("leche"))
    boton4.grid(row = 2, column = 4)
    
    boton5 = Button(xFrame, text = "Manzanas", width = 10, height = 2, command = lambda:combine_funcs("manzana"))
    boton5.grid(row = 2, column = 5)
    
    #------------------SEGUNDA FILA------------------
    
    
    boton6 = Button(xFrame, text = "Naranjas", width = 10, height = 2, command = lambda:combine_funcs("naranja"))
    boton6.grid(row = 3, column = 1)
    
    boton7 = Button(xFrame, text = "Platanos", width = 10, height = 2, command = lambda:combine_funcs("platano"))
    boton7.grid(row = 3, column = 2)
    
    boton8 = Button(xFrame, text = "Pollo", width = 10, height = 2, command = lambda:combine_funcs("pollo"))
    boton8.grid(row = 3, column = 3)
    
    boton9 = Button(xFrame, text = "Solomillo", width = 10, height = 2, command = lambda:combine_funcs("solomillo"))
    boton9.grid(row = 3, column = 4)
    
    boton10 = Button(xFrame, text = "Tomates", width = 10, height = 2, command = lambda:combine_funcs("tomate"))
    boton10.grid(row = 3, column = 5)
    
    boton11 = Button(xFrame, text = "Cerrar", width = 56, height = 2,command = newWindow.destroy)
    boton11.grid(row = 4, column = 1, columnspan = 5)

#------------------COMBINAR FUNCIONES---------------------
def combine_funcs(nombre): 
    ProjectFindFood.findFood(nombre)
    createListWindow()
    

#------------------Primera Ventana---------------------
window = Tk()

window.title("Frigorífico")
window.resizable(0,0)
window.geometry("400x590")

wFrame = Frame(window, width = 400, height = 600)
wFrame.grid(row=2, column=3)

bAbrir = Button(wFrame, text="Insertar Alimento en la Nevera",bg ="Gray", width = 60, height = 19, command = createNewWindow)
bCerrar= Button(wFrame, text="Cerrar Nevera",bg ="Gray", width = 60, height = 19, command = window.destroy)
bAbrir.grid(row = 0, column = 0)
bCerrar.grid(row = 1, column = 0)

window.mainloop()