try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import pandas as pd
import easygui as eg
from datetime import datetime
from tkcalendar import Calendar
# LIBRERIAS A UTILIZAR


"""class Test ():
    def __init__(self):
        self.rar= tk.Tk"""



def prueba(l):

    l=Label(raiz, text="PRUEBA").grid(pady=10, padx=15)


def forget (x):
    x.grid_forget()




# FUNCION PARA APARECER LOS PARAMETOS EN 'X' Y 'Y'
def retrieve (x,y):

    x.grid(row = 0, column = 0, ipady = 10, pady = 10, padx = 15)
    y.grid(row = 0, column = 1, ipady = 10, pady = 10, padx = 15)




# NUEVA VENTANA CON EL BOTON CONVERTIR
def ventanaconvertir():
    # CREAMOS UNA FUNCION PARA CONTENER TODA LA VENTANA DE CONVERTIR
    def convertitCSV():

        print(archivo2.get())
        # LEEMOS EL ARCHIVO A CONVERTIR
        dt = pd.read_csv(archivo2.get())

        # AL GUARDAR EL ARCHIVO CONVERTIMOS LE DAMOS TIEMPO DE FECHA DE CONVERSION
        time = str(datetime.today().strftime('%B %d %Y %H-%M-%S'))

        # CREAMOS VENTANA EMERGENTE PARA PEDRILE AL USUARIO A DONDE DESEA GUARDAR EL ARCHIVO CONVERTIDO
        directorio = eg.diropenbox(msg="EL ARCHIVO CSV:",
                                   title="DONDE DESEA GUARDAR",
                                   default='/home/')
        #LE COLOCAMOS UN NOMBRE POR DEFECTO AL ARCHIVO
        ruta = str(directorio + f"/GRAFICA ({str(time)}).csv")
        print(ruta)
        dt.to_csv(ruta)




# AL CREAR LA VENTANA DE CONVERTIR LE DEDEMOS ESPECIFICAR QUE DEBE ESTAR DENTRO DE LA VENTANA PRINCIPAL
    winCor = Toplevel(raiz)

# LE MANDAMOS EL TITULO DE LA VENTANA
    winCor.title("CONVERSION TXT A CSV")

# LE COLOCAMOS LAS POSICIONES DE LA VENTANA
    winCor.geometry("400x100")

# REDIMIENCIONAMOS LA VENTANA
    winCor.resizable(False,False)

# CREAMOS UN LABEL ESPESIFICANDO LA FACILIDAD DEL USUARIO
    etq = Label(winCor, text="Archivo A Convertir :")

# POSICIONES DEL LABEL
    etq.place(x=5, y=10)

# ENTRY PARA GUARDAR LA RUTA DEL ARCHIVO
    enlace2 = Entry(winCor, textvariable=archivo2).place(x=150, y=10, width=150, height=22)

# BOTON PARA CON LA FUNCION PARA BUSCAR EL ARCHIVO, JUNTO SUS PARAMETROS REQUERIDOS
    winCor.button = tk.Button(winCor, text="BUSCAR", command= lambda :archivo2.set(filedialog.askopenfilename(title="SELECCIONE EL ARCHIVO TXT : ", initialdir="/home/"))).place(x=315, y=6)

# BOTON PARA CONVERTIR EL ARCHIVO 'TXT' A 'CSV', JUNTO A SUS PARAMETROS REQUERIDOS
    con = tk.Button(winCor, text='Convertir a CSV..', command=convertitCSV , relief="raised", borderwidth=5)
    con.grid(row=0, column=0, sticky=W, ipady=0, ipadx=0, padx=150, pady=45)
    #mi_Entry = Entry(raiz, textvariable=archivo1).place(x=180, y=80, width=300, height=22)  # Creación de Entry buscar archivo

# CERRAMOS LA VENTANA DE CONVERTIR



raiz = Tk()


# SE MANDAN LOS PARAMETROS DE LA VENTANA PRINCIPAL

# TAMAÑO DE LA VENTANA
raiz.geometry("750x600")

# ESTE PARAMETRO NOS SIRVE PARA NO REDIMENZIONAR LA VENTANA
raiz.resizable(False,False)

# IMPORTAMOS UN INCON PARA NUESTRA VENTANA
#raiz.iconbitmap('E:\\PYTHON\\GUI\\img.ico')

# NOMBRE DE LA APP
raiz.title("App Graficación")

# IMAGEN DE FONDO DE LA PANTALLA PRINCIPAL
#imagen = PhotoImage(file = "fondo redi.png")

# MANDAMOS LOS PARAMETRO REQUERIDOS PARA NUESTRO FONDO DE LA PANTALLA PRINCIPAL

background = Label( text = "Imagen S.O de fondo")#image = imagen,
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# CREAMOS NUESTRO TITULO, JUNTO LE MANDAMOS LOS PARAMTROS REQUERIDOS

lb1=Label(raiz,  text="MONITOREO DE INVERNADERO ",   font=('Andale Mono', 25),foreground="black",background='white')#titulo de la pagina , su ubicacion, colores
lb1.place( x=180, y=25)

# CREAMOS UN TEXTO LLAMADO RUTA: JUNTOIS SUS PARAMETROS REQUERIDOS

lb2=Label(raiz,  text="RUTA",   font=('Andale Mono', 14),foreground="black",background='white')
lb2.place(x=170,y=102)



# CREAMOS ESTAS VARIABLES QUE HA FUTURO SON 3 BOTONES REQUERIDOS POR EL SISTEMA, LOS DECLARAMOS DE FORMA
# Stringvar() FORMA GLOBAL

b1=StringVar()
b2=StringVar()
b3=StringVar()
l=StringVar()
l=Label(raiz, text="asss").place(x=150, y=350)


# UTILIZAMOS LA PRIMERA VARIABLE B1 PARA UTILIZARLA DE FORMA BOTON, LE MANDAMOS EL CONTENIDO
# JUNTO A LA FUNCION FORGE CON SU CONTENIDO


b1 = Button(raiz, text = "FECHAS", command=  lambda : [forget(b2),retrieve(l,b1) ]) #boton fecha
b1.grid(row = 0, column = 1, ipadx = 0, ipady = 10, pady = 155, padx = 15)

# POSICIONAMOS EL BOTON


# UTILIZAMOS LA SEGUNDA VARIABLE B2 PARA UTILIZARLA DE FORMA BOTON, LE MANDAMOS EL CONTENIDO
# JUNTO A LA FUNCION FORGE CON SU CONTENIDO

b2 = Button(raiz, text = "DIAS", command = lambda : [forget(b1), retrieve(l,b1)])#boton dias
#b2.place(x=510,y=120)

# POSICIONAMOS EL BOTON
b2.grid(row = 0, column = 2, ipadx=0, ipady = 10, pady = 155, padx = 15)

# UTILIZAMOS LA TERCERA VARIABLE B3 PARA UTILIZARLA DE FORMA BOTON, LE MANDAMOS EL CONTENIDO
# JUNTO A LA FUNCION FORGE CON SU CONTENIDO

b3 = Button(raiz, text = "RESTABLECER", command = lambda : [retrieve(b1, b2), forget(l)])#BOTON RESTABLECER
b3.grid(row = 0, column = 3,ipadx=0, ipady = 10, pady = 155, padx = 15)

#BOTONES BOTONES BOTONES BOTONES BOTONES BOTONES BOTONES BOTONES BOTONES BOTONES

# CREAMOS ESTAS VARIABLES DE FORMA GLOBAL
archivo1 = StringVar()
archivo2 = StringVar()
enlace2 = StringVar()
url = StringVar()


# ESTE METODO  LO CREAMOS PARA PODER BUSCAR BUSCAR  EL ARCHIVO YA CONVERTIDO EN CSV, JUNTO LE MANDAMOS
# SUS PARAMETROS REQUERIDOS

raiz.button = tk.Button(raiz, text="BUSCAR",command= lambda :archivo1.set(filedialog.askopenfilename
(title="SELECCIONE EL ARCHIVO CSV : ", initialdir="/home/"))).place(x=550, y=97,width=80, height=35)                      #direccionamiento del boton BUSCAR

# CREAMOS UN ENTRY PARA PODER GUARDAR Y REFLEJAR LA RUTA DEL ARCHIVO IMPORTADO
mi_Entry = Entry(raiz,textvariable=archivo1).place( x=230, y=105, width=300, height=22) #Creación de Entry buscar archivo

# CREAMOS UN BOTON 'CONVERTIR' HACEMOS EL LLAMADO DE LA VENTANA DE CONVERTIR
btnconvertir = tk.Button(raiz, text="Convertir",command=ventanaconvertir)

# MANDAMOS SU POSICION
btnconvertir.place(x=650, y=97, width=80, height=35)
#btnconvertir.pack(padx=5, pady=100, ipadx=10, ipady=10) #direccionamiento con la funcion pack

#raiz.button = tk.Button(raiz, text="CONVERTIR").place(x=630, y=75) #BOTON CONVERTIR Y SU DIRECCIONAMIENTO
raiz.button = tk.Button(raiz, text="GRAFICAR").place(x=10, y=560) #BOTON GRAFICAR Y SU DIRECCIONAMIENTO


# CERRAMOS LA VENTANA PRINCIPAL
raiz.mainloop()