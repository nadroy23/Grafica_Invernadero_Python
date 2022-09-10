import pandas as pd
import easygui as eg
import tkinter as tk
from tkinter import ttk

from matplotlib import pyplot as plt
from tkcalendar import *
from datetime import datetime
from tkinter import filedialog
from tkinter import messagebox

def grafica(fecha1, fecha2, ruta):
    dt = pd.read_csv(ruta)
    df = pd.DataFrame(dt)

    # df.FECHA = pd.to_datetime(df.FECHA, format="%Y/%m/%d")
    print("----> -> "+ruta)
    pd.to_datetime(df.FECHA, format="%Y/%m/%d")

    #fecha1 = '2022-03-01'
    #fecha2 = '2022-03-15'

    rango = (df.FECHA >= fecha1) & (df.FECHA <= fecha2)
    df1 = df.loc[rango]
    pd.to_datetime(df1.FECHA, format="%Y/%m/%d")
    # print(df1)

    aux = None
    fch = []
    for i in df1.FECHA:
        if i != aux:
            aux = i
            fch.append(i)
    # print(fch)

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

    dtTrue = {'FECHA': fch,
              'T1': datos[0], 'T2': datos[1], 'T3': datos[2], 'T4': datos[3],
              'H1': datos[4], 'H2': datos[5], 'H3': datos[6], 'H4': datos[7],
              'MO1': datos[8], 'MO2': datos[9], 'MO3': datos[10], 'MO4': datos[11],
              'LUX1': datos[12], 'LUX2': datos[13], 'LUX3': datos[14], 'LUX4': datos[15], }

    df1 = pd.DataFrame(dtTrue)
    pd.to_datetime(df.FECHA, format="%Y/%m/%d")

    print(df1)
    fig, ax = plt.subplots(2, 2)
    ejex = 'FECHA'

    ax[0, 0].plot(df1[ejex], df1["T1"], color='blue', label='T1')
    ax[0, 0].plot(df1[ejex], df1["T2"], color='orange', label='T2')
    ax[0, 0].plot(df1[ejex], df1["T3"], color='green', label='T3')
    ax[0, 0].plot(df1[ejex], df1["T4"], color='red', label='T4')
    ax[0, 0].legend(loc='upper right')
    ax[0, 1].plot(df1[ejex], df1["H1"], color='orange', label='H1')
    ax[0, 1].plot(df1[ejex], df1["H2"], color='blue', label='H2')
    ax[0, 1].plot(df1[ejex], df1["H3"], color='green', label='H3')
    ax[0, 1].plot(df1[ejex], df1["H4"], color='red', label='H4')
    ax[0, 1].legend(loc='upper right')
    ax[1, 0].plot(df1[ejex], df1["MO1"], color='orange', label='MO1')
    ax[1, 0].plot(df1[ejex], df1["MO2"], color='blue', label='MO2')
    ax[1, 0].plot(df1[ejex], df1["MO3"], color='green', label='MO3')
    ax[1, 0].plot(df1[ejex], df1["MO4"], color='red', label='MO4')
    ax[1, 0].legend(loc='upper right')
    ax[1, 1].plot(df1[ejex], df1["LUX1"], color='orange', label='LUX1')
    ax[1, 1].plot(df1[ejex], df1["LUX2"], color='blue', label='LUX2')
    ax[1, 1].plot(df1[ejex], df1["LUX3"], color='green', label='LUX3')
    ax[1, 1].plot(df1[ejex], df1["LUX4"], color='red', label='LUX4')
    ax[1, 1].legend(loc='upper right')
    plt.show()


def alert(mensaje):
    messagebox.showinfo("Alerta", mensaje)


def convertitCSV():
    # print(archivo2.get().find("csv"))
    if (archivo2.get() == ""):
        alert("Debe selecionar un archivo...")
    elif (archivo2.get().find("csv") == (-1)):
        alert("Formato de archivo no valido...")
    else:
        dt = pd.read_csv(archivo2.get())

        time = str(datetime.today().strftime('%B %d %Y %H-%M-%S'))

        directorio = eg.diropenbox(msg="EL ARCHIVO CSV:",
                                   title="DONDE DESEA GUARDAR",
                                   default='/home/')
        ruta = str(directorio + f"/GRAFICA ({str(time)}).csv")
        # print(ruta)
        dt.to_csv(ruta)


def ventanaconvertir():
    winCor = tk.Toplevel(frameHead)
    winCor.title("CONVERSION TXT A CSV")
    winCor.geometry("400x100")
    winCor.resizable(False, False)
    ttk.Label(winCor, text="Archivo A Convertir :").place(x=5, y=10)
    ttk.Entry(winCor, textvariable=archivo2).place(x=150, y=10, width=150, height=22)
    winCor.button = tk.Button(winCor, text="BUSCAR", command=lambda: archivo2.set(
        filedialog.askopenfilename(title="SELECCIONE EL ARCHIVO TXT : ", initialdir="/home/"))).place(x=315, y=6)
    con = tk.Button(winCor, text='Convertir a CSV..', command=convertitCSV, relief="raised", borderwidth=5)
    con.grid(row=0, column=0, ipady=0, ipadx=0, padx=150, pady=45)
    winCor.grab_set()


def ocultar(btn, frame):
    btn.place_forget()
    frame.pack_forget()


def mostrarFrame(frame):
    frame.place(x=5, y=50)


def reset(btn1, btn2, fr1, fr2):
    fr1.place_forget()
    fr2.place_forget()
    date1.get_date()
    frameFooter.pack_forget()
    btn1.place(x=30, y=10, width=80, height=35)
    btn2.place(x=110, y=10, width=80, height=35)


def calendario(op, frame):
    global date1
    global date2
    global grafi
    frameFooter.pack(padx=5, pady=5)
    if op == 1:
        date1 = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2,
                          date_pattern='y/mm/dd', year=2022)
        date1.place(x=190, y=30, height=20)
        grafi = True
    else:

        ttk.Label(frame, text="Usar el siguiente rango.\n\nFecha1: 2022/03/01   <->   Fecha2: 2022/03/15 ",
                  foreground="black", background='white').place(x=140, y=15)

        date1 = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2,
                          date_pattern='y/mm/dd', year=2022)
        date1.place(x=100, y=80, height=20)

        date2 = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2,
                          date_pattern='y/mm/dd', year=2022)
        date2.place(x=260, y=80, height=20)
        grafi = False


def validar():
    if grafi:
        alert("Faltan ajustes para esta funcionalidad de graficar Dia... "+ str(date1.get_date()))
        #grafica(str(date1.get_date()))
    else:
        #alert("Grafica Fecha...  "+ str(date1.get_date()) + " <-> "+ str(date2.get_date()))
        if ruta.get() == "":
            print("---->1 -> " + ruta.get())
            alert("No se especifico una ruta se tomara un predeterminada...")
            grafica(str(date1.get_date()), str(date2.get_date()), str("../../Datos/datosTrue01.csv"))
            """elif (ruta.get().find("csv")):
            print("---->2 -> " + ruta.get())
            alert("Formato no valido...")"""
        else:
            print("---->3 -> " + ruta.get())
            grafica(str(date1.get_date()), str(date2.get_date()), ruta.get())




if __name__ == "__main__":
    root = tk.Tk()
    root.title("App Graficación")
    root.geometry("750x600")
    root.config(bg="CadetBlue1")

    grafi = tk.IntVar()
    archivo1 = tk.StringVar()
    archivo2 = tk.StringVar()
    enlace2 = tk.StringVar()
    url = tk.StringVar()

    frame = ttk.Frame(root).pack(padx=1, pady=1)

    frameHead = ttk.Frame(frame, width=730, height=150, relief="ridge")
    frameBody = ttk.Frame(frame, width=730, height=300, relief="ridge")
    frBodyF = ttk.Frame(frameBody, width=720, height=245, relief="ridge")
    frBodyD = ttk.Frame(frameBody, width=720, height=245, relief="ridge")
    frameFooter = ttk.Frame(frame, width=730, height=100, relief="ridge")

    ttk.Label(frameHead, text="MONITOREO DE INVERNADERO ", font=('Andale Mono', 25),
              foreground="black", background='white').place(x=110, y=25)
    ttk.Label(frameHead, text="RUTA:", font=('Andale Mono', 14),
              foreground="black", background='white').place(x=110, y=97, width=80, height=35)
    ruta = ttk.Entry(frameHead, textvariable=archivo1)
    ruta.place(x=200, y=105, width=300, height=22)
    ttk.Button(frameHead, text="BUSCAR", command=lambda: archivo1.set(filedialog.askopenfilename
                                                                      (title="SELECCIONE EL ARCHIVO CSV : ",
                                                                       initialdir="/home/"))).place(x=510, y=97,
                                                                                                    width=80, height=35)
    ttk.Button(frameHead, text="Convertir", command=ventanaconvertir).place(x=600, y=97, width=80, height=35)
    frameHead.pack(padx=5, pady=5)

    b1 = ttk.Button(frameBody, text="FECHAS",
                    command=lambda: [ocultar(b2, frBodyD), mostrarFrame(frBodyF), calendario(2, frBodyF)])
    b1.place(x=30, y=10, width=80, height=35)

    b2 = ttk.Button(frameBody, text="DIAS",
                    command=lambda: [ocultar(b1, frBodyF), mostrarFrame(frBodyD), calendario(1, frBodyD)])
    b2.place(x=110, y=10, width=80, height=35)

    b3 = ttk.Button(frameBody, text="RESTABLECER", command=lambda: [reset(b1, b2, frBodyF, frBodyD, )])
    b3.place(x=190, y=10, width=90, height=35)

    frameBody.pack(padx=5, pady=5)

    tk.Button(frameFooter, text="GRAFICAR", command=lambda: validar()).place(x=10, y=40)

    root.mainloop()
