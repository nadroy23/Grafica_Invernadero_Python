
import pandas as pd
import easygui as eg
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from datetime import datetime
from tkinter import filedialog
from tkinter import messagebox


def alert(mensaje):
    messagebox.showinfo("Alerta",mensaje)


def convertitCSV():
    print(archivo2.get().find("csv"))
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
        print(ruta)
        dt.to_csv(ruta)

def ventanaconvertir():
    winCor = tk.Toplevel(frameHead)
    winCor.title("CONVERSION TXT A CSV")
    winCor.geometry("400x100")
    winCor.resizable(False,False)
    ttk.Label(winCor, text="Archivo A Convertir :").place(x=5, y=10)
    ttk.Entry(winCor, textvariable=archivo2).place(x=150, y=10, width=150, height=22)
    winCor.button = tk.Button(winCor, text="BUSCAR", command= lambda :archivo2.set(filedialog.askopenfilename(title="SELECCIONE EL ARCHIVO TXT : ", initialdir="/home/"))).place(x=315, y=6)
    con = tk.Button(winCor, text='Convertir a CSV..', command=convertitCSV , relief="raised", borderwidth=5)
    con.grid(row=0, column=0, ipady=0, ipadx=0, padx=150, pady=45)



def magia(id,btn, frame1, frame2):
    if id == 1:
        #b2.place(x=115, y=20, width=80, height=35)
        btn.pack
        frame2.pack_forget()
        frame1.pack()
    elif id == 2:
        #b1.place(x=30, y=20, width=80, height=35)

        frame2.pack_forget()
        frame1.pack()
    else:
        b1.place(x=30, y=20, width=80, height=35)
        b2.place(x=115, y=20, width=80, height=35)
        frame1.forget()



if __name__ == "__main__":
    root = tk.Tk()

    root.title("App Graficación")
    root.geometry("750x600")
    root.config(bg="CadetBlue1")

    b1 = tk.StringVar()
    b2 = tk.StringVar()
    b3 = tk.StringVar()
    archivo1 = tk.StringVar()
    archivo2 = tk.StringVar()
    enlace2 = tk.StringVar()
    url = tk.StringVar()

    frame = ttk.Frame(root).pack(padx = 1, pady = 1)

    frameHead = ttk.Frame(frame, width = 730, height = 150, relief = "ridge")
    frameBody = ttk.Frame(frame, width = 730, height = 300, relief = "ridge")
    frBodyF = ttk.Frame(frameBody, width=700, height=270, relief="ridge")
    frBodyD = ttk.Frame(frameBody, width=700, height=270, relief="ridge")
    frameFooter = ttk.Frame(frame, width = 730, height = 100, relief = "ridge")


    ttk.Label(frameHead, text="MONITOREO DE INVERNADERO ", font=('Andale Mono', 25),
              foreground="black", background='white').place(x=110, y=25)
    ttk.Label(frameHead, text="RUTA:", font=('Andale Mono', 14),
              foreground="black", background='white').place(x=110, y=97, width=80, height=35)
    ttk.Entry(frameHead, textvariable=archivo1).place(x=200, y=105, width=300, height=22)
    ttk.Button(frameHead, text="BUSCAR", command= lambda: archivo1.set(filedialog.askopenfilename
                        (title="SELECCIONE EL ARCHIVO CSV : ", initialdir="/home/"))).place(x=510, y=97,
                        width=80, height=35)
    ttk.Button(frameHead, text="Convertir", command= lambda: ventanaconvertir).place(x=600, y=97, width=80, height=35)
    frameHead.pack(padx=5, pady=5)

    b1 = ttk.Button(frameBody, text="FECHAS", command= lambda: magia(1, b2, frBodyF, frBodyD)).pack()

    b2 = ttk.Button(frameBody, text="DIAS", command= lambda: magia(2, b1, frBodyD, frBodyF)).pack()

    b3 = ttk.Button(frameBody, text="RESTABLECER").place(x=200, y=20,
                        width=80, height=35)

    #frBody.pack(padx = 5, pady = 5)
    frameBody.pack(padx=5, pady=5)

    tk.Button(frameFooter, text="GRAFICAR").place(x=10, y=40)
    frameFooter.pack(padx = 5, pady = 5)

    root.mainloop()