"""
DESCRIPCION DEL PROYECTO:

Originario, de una necesidad actual su objetivo principal es solventar al pequeño o grande agricultor,
trabajando de la mano de sistemas de informacion, implementando un sistema de monitoreo para invernadero

LENGUAJE:
Python es un lenguaje de programación que te permite trabajar rápidamente
e integrar los sistemas de manera más eficaz,ademas ceunta con multiparadigmas.

@Autores:
Anderson Cardozo Arrieta
Yordan Tarazona
Mauricio Zafra Aycardi
Jorge Sequeda Serrano

"""

"""
LIBRERIAS

Pandas: Pandas, es una libreria que proporciona estructura de datos y herramientas de analisis
de informacion almacenada en hojas de calculo, base de datos etc. 

EasyGUI: EasyGUI, es un módulo para una programación GUI muy simple y fácil en Python, Permitiendo incorporar
los scripts a una interfaz grafica.

Tkinter: Tkinter, es el paquete GUI (interfaz gráfica de usuario) 
estándar de facto de Python. Es una capa delgada orientada a objetos.

Matplotlib: Matplotlib, es una biblioteca completa para crear visualizaciones estáticas,
animadas e interactivas en Python.

Tkcalendar: Tkcalendar es un módulo de Python que proporciona los widgets Calendar y DateEntry para Tkinter.

Datetime: Datetime, es un modulo proporcionando clases para manipular fechas y horas,la implementación
está en la extracción eficiente de atributos para el formato y la manipulación de la salida.
"""

import pandas as pd
import easygui as eg
import tkinter as tk
from tkinter import ttk
from matplotlib import pyplot as plt
from tkcalendar import *
from datetime import datetime
from tkinter import filedialog
from tkinter import messagebox

"""
FUNCION

Nombre: grafica

Recibe: los parametros, fecha1, fecha2, ruta

Retorna: No retorna ninguna funcionalidad

Funcionalidad:
"""

def graficar(title,condi,df1, ejex):
    fig, ax = plt.subplots(2, 2)
    fig.suptitle(title)
    ax[0, 0].plot(df1[ejex], df1["T1"], 'b-*', label='T1')
    ax[0, 0].plot(df1[ejex], df1["T2"], 'r-o', label='T2')
    ax[0, 0].plot(df1[ejex], df1["T3"], 'c-*', label='T3')
    ax[0, 0].plot(df1[ejex], df1["T4"], 'm-o', label='T4')
    ax[0, 0].set_title('TEMPERATURA')
    ax[0, 0].set(ylabel='Temperatura')
    ax[0, 0].legend(loc='upper right')

    ax[0, 1].plot(df1[ejex], df1["H1"], 'b-*', label='H1')
    ax[0, 1].plot(df1[ejex], df1["H2"], 'r-o', label='H2')
    ax[0, 1].plot(df1[ejex], df1["H3"], 'c-*', label='H3')
    ax[0, 1].plot(df1[ejex], df1["H4"], 'm-o', label='H4')
    ax[0, 1].set_title('HUMEDAD')
    ax[0, 1].set(ylabel='Humedad')
    ax[0, 1].legend(loc='upper right')

    ax[1, 0].plot(df1[ejex], df1["MO1"], 'b-*', label='MO1')
    ax[1, 0].plot(df1[ejex], df1["MO2"], 'r-o', label='MO2')
    ax[1, 0].plot(df1[ejex], df1["MO3"], 'c-*', label='MO3')
    ax[1, 0].plot(df1[ejex], df1["MO4"], 'm-o', label='MO4')
    ax[1, 0].set_title('MO')
    ax[1, 0].set(xlabel=condi, ylabel='MO')
    ax[1, 0].legend(loc='upper right')

    ax[1, 1].plot(df1[ejex], df1["LUX1"], 'b-*', label='LUX1')
    ax[1, 1].plot(df1[ejex], df1["LUX2"], 'r-o', label='LUX2')
    ax[1, 1].plot(df1[ejex], df1["LUX3"], 'c-*', label='LUX3')
    ax[1, 1].plot(df1[ejex], df1["LUX4"], 'm-o', label='LUX4')
    ax[1, 1].set_title('LUMINOSIDAD')
    ax[1, 1].set(xlabel=condi, ylabel='Luminosidad')
    ax[1, 1].legend(loc='upper right')
    plt.show()


def grafica(fecha, ruta):
    dt = pd.read_csv(ruta)
    df = pd.DataFrame(dt)

    # df.FECHA = pd.to_datetime(df.FECHA, format="%Y/%m/%d")
    print("----> -> " + ruta)
    pd.to_datetime(df.FECHA, format="%Y/%m/%d")

    # fecha1 = '2022-03-01'
    # fecha2 = '2022-03-15'
    if len(fecha) > 1:
        fecha1 = fecha[0]
        fecha2 = fecha[1]

        rango = (df.FECHA >= fecha1) & (df.FECHA <= fecha2)
        df1 = df.loc[rango]
        pd.to_datetime(df1.FECHA, format="%Y/%m/%d")
        # print(df1)

        aux = None
        fch = []
        fchx = []
        for i in df1.FECHA:
            if i != aux:
                aux = i
                fch.append(i)
                fchx.append(i[5:])
        print(len(fch))

        print('Row count is:', len(df1.index))
        datos = []
        aux = []
        df2 = df1
        for i in df2:
            if i != 'FECHA':
                for j in range(0, len(fch)):
                    rango = (df.FECHA == fch[j])
                    df1 = df.loc[rango]
                    aux.append(df1[i].mean())
                datos.append(aux)
                aux = []
        title = 'Graficación X Rango de Fechas'
        condi = 'Fechas'
    else:
        fecha1 = fecha[0]
        fecha2 = fecha[0]

        rango = (df.FECHA >= fecha1) & (df.FECHA <= fecha2)
        df1 = df.loc[rango]
        pd.to_datetime(df1.FECHA, format="%Y/%m/%d")

        print('Row count is:', len(df1['T1'].index))
        datos = []
        aux = []
        fchx = []
        df2 = df1
        cont = 0
        suma = 0
        for i in df2:
            if i != 'FECHA':
                for j in df2[i]:
                    if cont >= (len(df1[i].index)/12):
                        #print(cont)
                        aux.append(suma/cont)
                        cont = 0
                        suma = 0
                        i#f len(fchx) <= 11:
                            #fchx.append(fchx[-1]+1)
                    #print('**********************>>  '+str(j))
                    suma += j
                    cont += 1
                    #print(cont)
                datos.append(aux)
                aux = []
        datos[0].append(1)
        for i in range(0, len(datos[0])):
            fchx.append(i+1)
        print('==================>>  ' + str(len(fchx)))
        print('==================>>  '+str(len(datos[0])))
        print('==================>>  ' + str(len(datos[2])))
        print('==================>>  ' + str(len(datos[3])))
        print('==================>>  ' + str(len(datos[4])))
        print(cont)
        title = 'Graficación X Dia'
        condi = 'Horas'

    dtTrue = {'FECHA': fchx,
              'T1': datos[0], 'T2': datos[1], 'T3': datos[2], 'T4': datos[3],
              'H1': datos[4], 'H2': datos[5], 'H3': datos[6], 'H4': datos[7],
              'MO1': datos[8], 'MO2': datos[9], 'MO3': datos[10], 'MO4': datos[11],
              'LUX1': datos[12], 'LUX2': datos[13], 'LUX3': datos[14], 'LUX4': datos[15], }

    df1 = pd.DataFrame(dtTrue)
    pd.to_datetime(df.FECHA, format="%Y/%m/%d")

    print(df1)
    ejex = 'FECHA'
    graficar(title, condi, df1, ejex)




"""
FUNCION

Nombre: mensaje

Recibe: el parametro, alerta

Retorna: no retorna ninguna funcionalidad

Funcionalidad: Se emplea para informar al usuario sobre alguna cuestión
o bien exhortarlo a tomar una decisión.
"""


def alert(mensaje):
    messagebox.showinfo("Alerta", mensaje)


"""
FUNCION

Nombre: convertitCSV

Recibe: No recibe ningun parametro

Retorna: no retorna ninguna funcionalidad

Funcionalidad: validacion, del archivo plano al convertirlo, con un formato requerido 
para impedir configuraciones no deseadas. asmimos guardar el archivo convertido Csv en el SO.

"""


def convertitCSV():
    # print(archivo2.get().find("csv"))
    if (archivo2.get() == ""):
        alert("SELECCIONE UN ARCHIVO")
    elif (archivo2.get().find("csv") == (-1)):
        alert(" FORMATO DE ARCHIVO NO VALIDO...")
    else:
        dt = pd.read_csv(archivo2.get())

        time = str(datetime.today().strftime('%B %d %Y %H-%M-%S'))

        directorio = eg.diropenbox(msg="EL ARCHIVO CSV",
                                   title="DONDE DESEA GUARDAR",
                                   default='/home/')
        ruta = str(directorio + f"/GRAFICA ({str(time)}).csv")
        # print(ruta)
        dt.to_csv(ruta)


"""
FUNCION

Nombre: ventanaconvertir

Recibe: No recibe ningun parametro

Retorna: no retorna ninguna funcionalidad

Funcionalidad: Disponer, una ventana apartada para la conversion del archivo Txt a Csv, 


"""


def ventanaconvertir():
    winCor = tk.Toplevel(frameHead)
    winCor.title("CONVERSION TXT A CSV")
    winCor.geometry("400x100")
    winCor.resizable(False, False)
    ttk.Label(winCor, text="Archivo A Convertir :").place(x=5, y=10)
    ttk.Entry(winCor, textvariable=archivo2).place(x=150, y=10, width=150, height=22)
    winCor.button = tk.Button(winCor, text="BUSCAR", command=lambda: archivo2.set (filedialog.askopenfilename(title="SELECCIONE EL ARCHIVO TXT  ", initialdir="/home/"))).place(x=315, y=6)
    con = tk.Button(winCor, text='Convertir a CSV', command=convertitCSV, relief="raised", borderwidth=5)
    con.grid(row=0, column=0, ipady=0, ipadx=0, padx=150, pady=45)
    winCor.grab_set()


def ocultar(btn, frame):
    btn.place_forget()
    frame.pack_forget()


def mostrarFrame(frame):
    frame.place(x=5, y=100)


def reset(btn1, btn2, fr1, fr2):
    fr1.place_forget()
    fr2.place_forget()
    date1.get_date()
    frameFooter.pack_forget()
    btn1.place(x=30, y=50, width=80, height=35)
    btn2.place(x=110, y=50, width=80, height=35)


def calendario(op, frame):
    global date1
    global date2
    global grafi
    frameFooter.pack(padx=5, pady=10)
    if op == 1:
        date1 = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2,
                          date_pattern='y/mm/dd', year=2022, month=3, day=1)
        date1.place(x=190, y=30, height=20)
        grafi = True
    else:

        #ttk.Label(frame, text="USAR EL SIGUIENTE RANGO\n\nFecha1: 2022/03/01   <->   Fecha2: 2022/03/15 ",
                  #foreground="black", background='white').place(x=140, y=15)

        date1 = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2,
                          date_pattern='y/mm/dd', year=2022, month=3, day=1)
        date1.place(x=100, y=80, height=20)

        date2 = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2,
                          date_pattern='y/mm/dd', year=2022, month=3, day=15)
        date2.place(x=260, y=80, height=20)
        grafi = False


def validar():
    if grafi:
        #alert("Faltan ajustes para esta funcionalidad de graficar Dia... " + str(date1.get_date()))
        if ruta.get() == "":
            print("---->1 -> " + ruta.get())
            alert("No se especifico una ruta se tomara un predeterminada...")
            grafica([str(date1.get_date())], str("../../Datos/datosTrue01.csv"))
        else:
            print("---->3 -> " + ruta.get())
            grafica([str(date1.get_date())], ruta.get())
    else:
        # alert("Grafica Fecha...  "+ str(date1.get_date()) + " <-> "+ str(date2.get_date()))
        if ruta.get() == "":
            print("---->1 -> " + ruta.get())
            alert("No se especifico una ruta se tomara un predeterminada...")
            #grafica([str(date1.get_date())], str("../../Datos/datosTrue01.csv"))
            grafica([str(date1.get_date()), str(date2.get_date())], str("../../Datos/datosTrue01.csv"))
            """elif (ruta.get().find("csv")):
            print("---->2 -> " + ruta.get())
            alert("Formato no valido...")"""
        else:
            print("---->3 -> " + ruta.get())
            grafica([str(date1.get_date()), str(date2.get_date())], ruta.get())


if __name__ == "__main__":
    root = tk.Tk()
    root.title("@YORANDE")
    root.geometry("750x540")
    root.resizable(False, False)
    root.config(bg="CadetBlue1")
    #root.iconbitmap('D:\\Usuarios\\Yordan Tarazona\\Desktop\\Expo\\Grafica_Invernadero_Python\\Diseño\\fondo\\ICO.ico')
    #imagen = tk.PhotoImage(file="D:\\Usuarios\\Yordan Tarazona\\Desktop\\Expo\\Grafica_Invernadero_Python\\Diseño\\fondo.png")
    #background = tk.Label(image=imagen, text="Imagen S.O de fondo")
    #background.place(x=0, y=0, relwidth=1, relheight=1)

    grafi = tk.IntVar()
    archivo1 = tk.StringVar()
    archivo2 = tk.StringVar()
    enlace2 = tk.StringVar()
    url = tk.StringVar()


    frame = tk.Frame(root).place()

    frameHead = tk.Frame(frame, width=900, height=80, background="white")
    frameBody = tk.Frame(frame, width=665, height=320, background="white")
    frBodyF = tk.Frame(frameBody, width=720, height=195, background="white")
    frBodyD = tk.Frame(frameBody, width=720, height=195, background="white")
    frameFooter = tk.Frame(frame, width=730, height=45, background="white")

    ttk.Label(frameHead, text="MONITOREO DE INVERNADERO", font=('Andale Mono', 23),
              foreground="black", background='white').place(x=10, y=25)
    ttk.Label(frameBody, text="RUTA", font=('Andale Mono', 14),
              foreground="black", background="white").place(x=10, y=10, width=80, height=35)
    ruta = ttk.Entry(frameBody, textvariable=archivo1)
    ruta.place(x=80, y=17, width=400, height=22)
    tk.Button(frameBody, text="BUSCAR", foreground="black", bg="gold2", command=lambda: archivo1.set(filedialog.askopenfilename
    (title="SELECCIONE EL ARCHIVO CSV ", initialdir="/home/"))).place(x=490, y=10,width=80, height=35)
    tk.Button(frameBody, text="Convertir",foreground="black", bg="gold2", command=ventanaconvertir).place(x=580, y=10, width=80, height=35)
    frameHead.pack(padx=130, pady=5)


    b1 = tk.Button(frameBody, text="FECHAS", foreground="black", bg="gold2",
                    command=lambda: [ocultar(b2, frBodyD), mostrarFrame(frBodyF), calendario(2, frBodyF)])
    b1.place(x=30, y=50, width=80, height=35)

    b2 = tk.Button(frameBody, text="DIAS", foreground="black", bg="gold2",
                    command=lambda: [ocultar(b1, frBodyF), mostrarFrame(frBodyD), calendario(1, frBodyD)])
    b2.place(x=110, y=50, width=80, height=35)

    b3 = tk.Button(frameBody, text="RESTABLECER", foreground="black", bg="gold2", command=lambda: [reset(b1, b2, frBodyF, frBodyD)])
    b3.place(x=190, y=50, width=90, height=35)

    frameBody.pack(padx=5, pady=30)

    tk.Button(frameFooter, text="GRAFICAR", bg="gold2" ,command=lambda: validar()).place(x=10, y=8)

    root.mainloop()
