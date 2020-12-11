
import tkinter
from builtins import list
from tkinter import *
import pickle

'''
Elemento Contacto (Clase)
'''
class Contacto():
    def __init__(self, nombre, apellidos, telefono):
        self.nombre=nombre
        self.apellidos=apellidos
        self.telefono=telefono

    def print(self):
        return "{}-{}-{}-{}".format(self.nombre, self.apellidos,self.telefono,self.id)

    def __str__(self):
        return "{}-{}-{}-{}".format(self.nombre, self.apellidos,self.telefono,self.id)

    def extraer(self):
        return "{}-{}-{}-{}".format(self.nombre, self.apellidos,self.telefono,self.id)

    def setid(self,id):
        self.id= id
    def getNombre(self):
        return self.nombre
    def getApellidos(self):
        return self.apellidos
    def getTelefono(self):
        return self.telefono
    def getId(self):
        return self.id

'''
Lista de contactos (clase)
'''
class ListaContactos:
    contactos=[]

    def __init__(self):
        try:
            #abrimos el fichero y nos situamos en el inicio
            listaDeContactos=open("fichero_contactos", "ab+")
            listaDeContactos.seek(0)

            #cargamos el fichero
            self.contactos=pickle.load(listaDeContactos)
            print("Cargados {} contactos".format(len(self.contactos)))
        except:
            print("Fichero vacío")
        finally:
            listaDeContactos.close()
            del(listaDeContactos)

    def guardarContactosFichero(self):
        #abrimos el fichero
        listaDeContactos = open("fichero_contactos", "wb")
        #Volcamos el contenido del fichero en la lista
        pickle.dump(self.contactos, listaDeContactos)
        listaDeContactos.close()
        del (listaDeContactos)

    def aniadirContacto(self,contacto):
        id = len(self.contactos) + 1
        contacto.setid(id)
        #se añade el contacto a la lista y se actualiza el fichero
        self.contactos.append(contacto)
        self.guardarContactosFichero()
    def borrarContacto(self,id):
        if(int(id)<=len(self.contactos)):
            try:
                self.contactos.pop(int(id)-1)
            except:
                print("No existe el contacto")
            #Se cambia el id de los demás contactos
            try:
                self.contactos[0].setid(0)
            except:
                print()
            contador=0
            for i in self.contactos:

                contador= contador+1
                if contador>=int(id) and contador<len(self.contactos)+1:
                    i.setid(contador-1)
            self.guardarContactosFichero()
    def modificarContactos(self,contacto,id):
        if (int(id) <= len(self.contactos)):
            self.contactos.pop(int(id-1))
            contacto.setid(id)
            self.contactos.insert(id-1,contacto)
            self.guardarContactosFichero()

    def mostrarContactos(self):
        for item in self.contactos:
            print(item)
    def verDatos(self):
        listaDeContactos = open("fichero_contactos", "rb")
        lista = pickle.load(listaDeContactos)
        listaDeContactos.close()
        del (listaDeContactos)
        datos = ""
        for contacto in lista:
            datos = datos + contacto.extraer() + "\n"
        cajaNombre = Text(ventana)
        cajaNombre.insert(END, datos)
        cajaNombre.configure(state="disabled")
        cajaNombre.grid(row=5, columnspan=6)

'''
Métodos para los botones
'''
listaContactos = ListaContactos()
def nuevoContacto():
    nombre= tfNombre.get()
    apellidos= tfApellidos.get()
    telefono= tfTelefono.get()
    
    contacto = Contacto(nombre,apellidos,telefono)
    listaContactos.aniadirContacto(contacto)
    listaContactos.verDatos()

def eliminarContacto():
    id= tfId.get()

    listaContactos.borrarContacto(id)
    listaContactos.verDatos()
def modificarContacto():
    nombre = tfNombre.get()
    apellidos = tfApellidos.get()
    telefono = tfTelefono.get()
    id = tfId.get()

    contacto = Contacto(nombre, apellidos, telefono)
    listaContactos.modificarContactos(contacto,int(id))
    listaContactos.verDatos()

'''
Entorno gráfico
'''
ventana = tkinter.Tk()
ventana.geometry("600x400")

lbSep=tkinter.Label(ventana,text= "")
lbNombre = tkinter.Label(ventana,text="Nombre: ")
lbApellidos = tkinter.Label(ventana,text="Apellidos: ")
lbTelefono = tkinter.Label(ventana,text="Telefono: ")
lbId= tkinter.Label(ventana,text="Id: ")
tfNombre = tkinter.Entry(ventana)
tfApellidos = tkinter.Entry(ventana)
tfTelefono = tkinter.Entry(ventana)
tfId = tkinter.Entry(ventana)

lbNombre.grid(row=0,column=1)
lbApellidos.grid(row=1,column=1)
lbTelefono.grid(row=2,column=1)
lbId.grid(row=1,column=3)
tfNombre.grid(padx=5, pady=5,row=0,column=2)
tfApellidos.grid(padx=5, pady=5,row=1,column=2)
tfTelefono.grid(padx=5, pady=5,row=2,column=2)
tfId.grid(padx=5, pady=5,row=1,column=4)


btnAniadir=tkinter.Button(ventana,text="Añadir",command=nuevoContacto)
btnBorrar=tkinter.Button(ventana,text="Borrar",command=eliminarContacto)
btnModif=tkinter.Button(ventana,text="Modificar",command=modificarContacto)

lbSep.grid(row=3,column=0)
btnAniadir.grid(row=4,column=1)
btnBorrar.grid(row=4,column=2)
btnModif.grid(row=4,column=3)

listaContactos.verDatos()

ventana.mainloop()
