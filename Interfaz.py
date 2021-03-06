from tkinter import*
from string import*
from tkinter import messagebox,ttk,filedialog
from os import startfile


FrameInicio=Tk()
FrameInicio.geometry("597x450")
FrameInicio.title("Zoológico de San Diego, California // Consulta de Animales")

#Funcion que ense;a el Acerca De de la programacion, unica para el menu
#Se utilizan labels

def acercade():
    filewin = Toplevel(FrameInicio)
    info = Label(filewin, text="Programacion de Comercio Electronico",font=20)
    info1 = Label(filewin, text="eCart V.4.0.")
    info2 = Label(filewin, text="Una tienda electronica hecha con TKinter y Python")
    info3 = Label(filewin, text="Diseñador: Luis Diego Conejo Mora")
    info4 = Label(filewin, text="Programada por: Luis Diego Conejo Mora")
    info5 = Label(filewin, text="eCart, tus compras, al instante")
    info6 = Label(filewin, text="Copyright © 05/2011")
    info.pack()
    info2.pack()
    info3.pack()
    info4.pack()
    info5.pack()
    info6.pack()

def mantenimiento():
    fondo=Canvas(FrameInicio,width=597,height=309,bg="white")
    fondo.place(x=0,y=141)
    
    varraza=StringVar()
    a=open("animal.txt","r")
    datos=a.read()
    lista1=str.split(datos,"\n")
    listaraza=ttk.Combobox(state="readonly",values=lista1,textvariable=varraza)
    listaraza.place(x=200,y=150)
    varraza.set("Elija una raza")
    labelraza=Label(bg='white',fg='black',text="Raza:")
    labelraza.place(x=90,y=150)
    labelind1=Label(bg='white',fg="red",text="Elija una raza  (Estan subdivididas en Anfibios, Aves, Mamiferos, Reptiles e Insectos)",font=("Arial",8))
    labelind1.place(x=90,y=170)
    
    varedad=StringVar()
    lista2=[]
    for i in range(0,100):
        lista2.append(i)
    listaedad=ttk.Combobox(state="readonly",values=lista2,textvariable=varedad)
    listaedad.place(x=200,y=190)
    varedad.set("Elija una edad")
    labeledad=Label(bg='white',fg='black',text="Edad:")
    labeledad.place(x=90,y=190)
    labelind2=Label(bg='white',fg="red",text="Elija la edad del animal",font=("Arial",8))
    labelind2.place(x=90,y=210)

    vargenero=StringVar()
    lista3=["Macho","Hembra","Asexual"]
    listagenero=ttk.Combobox(state="readonly",values=lista3,textvariable=vargenero)
    listagenero.place(x=200,y=230)
    vargenero.set("Elija un genero")
    labelgenero=Label(bg='white',fg='black',text="Género:")
    labelgenero.place(x=90,y=230)
    labelind3=Label(bg='white',fg="red",text="Elija el género del animal",font=("Arial",8))
    labelind3.place(x=90,y=250)

    varnombre=StringVar()
    entrynombre=Entry(bg='white',fg='black',width=30,textvariable=varnombre)
    entrynombre.place(x=200,y=270)
    labelnombre=Label(bg='white',fg='black',text="Nombre:")
    labelnombre.place(x=90,y=270)
    labelind4=Label(bg='white',fg="red",text="Escriba el nombre del animal",font=("Arial",8))
    labelind4.place(x=90,y=290)

    vareco=StringVar()
    b=open("ecosistema.txt","r")
    datos2=b.read()
    lista4=str.split(datos2,"\n")
    listaeco=ttk.Combobox(state="readonly",values=lista4,textvariable=vareco)
    listaeco.place(x=200,y=310)
    vareco.set("Elija un ecosistema")
    labeleco=Label(bg='white',fg='black',text="Ecosistema:")
    labeleco.place(x=90,y=310)
    labelind5=Label(bg='white',fg="red",text="Elija el ecosistema original del animal",font=("Arial",8))
    labelind5.place(x=90,y=330)

    varcomida=StringVar()
    entrycomida=Entry(bg='white',fg='black',width=30,textvariable=varcomida)
    entrycomida.place(x=200,y=350)
    labelcomida=Label(bg='white',fg='black',text="Comida:")
    labelcomida.place(x=90,y=350)
    labelind6=Label(bg='white',fg="red",text="Escriba la comida favorita del animal",font=("Arial",8))
    labelind6.place(x=90,y=370)

    botonconsulta=Button(bg="green",fg="black",text="Consulta",command=consulta)
    botonconsulta.place(x=430,y=250)

    def agregar():
        pass
    def borrar():
        varraza.set("Elija una raza")
        varedad.set("Elija una edad")
        vareco.set("Elija un ecosistema")
        varcomida.set("")
        varnombre.set("")
        vargenero.set("Elija un genero")
    botonagregar=Button(bg="green",fg="black",text="Agregar Animal",command=agregar)
    botonagregar.place(x=200,y=400)

    botonborrar=Button(bg="green",fg="black",text="Borrar datos",command=borrar)
    botonborrar.place(x=300,y=400)

def consulta():
    fondo=Canvas(FrameInicio,width=597,height=309,bg="white")
    fondo.place(x=0,y=141)
    
    varraza=StringVar()
    a=open("animal.txt","r")
    datos=a.read()
    lista1=str.split(datos,"\n")
    listaraza=ttk.Combobox(state="readonly",values=lista1,textvariable=varraza)
    listaraza.place(x=200,y=150)
    varraza.set("Elija una raza")
    labelraza=Label(bg='white',fg='black',text="Raza:")
    labelraza.place(x=90,y=150)
    labelind1=Label(bg='white',fg="red",text="Elija una raza  (Estan subdivididas en Anfibios, Aves, Mamiferos, Reptiles e Insectos)",font=("Arial",8))
    labelind1.place(x=90,y=170)
    
    varedad=StringVar()
    lista2=[]
    for i in range(0,100):
        lista2.append(i)
    listaedad=ttk.Combobox(state="readonly",values=lista2,textvariable=varedad)
    listaedad.place(x=200,y=190)
    varedad.set("Elija una edad")
    labeledad=Label(bg='white',fg='black',text="Edad:")
    labeledad.place(x=90,y=190)
    labelind2=Label(bg='white',fg="red",text="Elija la edad del animal",font=("Arial",8))
    labelind2.place(x=90,y=210)

    vargenero=StringVar()
    lista3=["Macho","Hembra","Asexual"]
    listagenero=ttk.Combobox(state="readonly",values=lista3,textvariable=vargenero)
    listagenero.place(x=200,y=230)
    vargenero.set("Elija un genero")
    labelgenero=Label(bg='white',fg='black',text="Género:")
    labelgenero.place(x=90,y=230)
    labelind3=Label(bg='white',fg="red",text="Elija el género del animal",font=("Arial",8))
    labelind3.place(x=90,y=250)

    varnombre=StringVar()
    entrynombre=Entry(bg='white',fg='black',width=30,textvariable=varnombre)
    entrynombre.place(x=200,y=270)
    labelnombre=Label(bg='white',fg='black',text="Nombre:")
    labelnombre.place(x=90,y=270)
    labelind4=Label(bg='white',fg="red",text="Escriba el nombre del animal",font=("Arial",8))
    labelind4.place(x=90,y=290)

    vareco=StringVar()
    b=open("ecosistema.txt","r")
    datos2=b.read()
    lista4=str.split(datos2,"\n")
    listaeco=ttk.Combobox(state="readonly",values=lista4,textvariable=vareco)
    listaeco.place(x=200,y=310)
    vareco.set("Elija un ecosistema")
    labeleco=Label(bg='white',fg='black',text="Ecosistema:")
    labeleco.place(x=90,y=310)
    labelind5=Label(bg='white',fg="red",text="Elija el ecosistema original del animal",font=("Arial",8))
    labelind5.place(x=90,y=330)

    varcomida=StringVar()
    entrycomida=Entry(bg='white',fg='black',width=30,textvariable=varcomida)
    entrycomida.place(x=200,y=350)
    labelcomida=Label(bg='white',fg='black',text="Comida:")
    labelcomida.place(x=90,y=350)
    labelind6=Label(bg='white',fg="red",text="Escriba la comida favorita del animal",font=("Arial",8))
    labelind6.place(x=90,y=370)

    botonmante=Button(bg="green",fg="black",text="Mantenimiento",command=mantenimiento)
    botonmante.place(x=430,y=250)

    def consultar():
        pass
    def borrar():
        varraza.set("Elija una raza")
        varedad.set("Elija una edad")
        vareco.set("Elija un ecosistema")
        varcomida.set("")
        varnombre.set("")
        vargenero.set("Elija un genero")
    botonconsultar=Button(bg="green",fg="black",text="Consultar",command=consultar)
    botonconsultar.place(x=200,y=400)

    botonborrar=Button(bg="green",fg="black",text="Borrar datos",command=borrar)
    botonborrar.place(x=300,y=400)

    
    
fondor=Canvas(FrameInicio,width=597,height=450,bg="white")
fondor.place(x=0,y=0)
photo = PhotoImage(file="header.gif")
labelimagen=Label(FrameInicio,image=photo)
labelimagen.place(x=0,y=0)

labelinst=Label(bg="white",text="BIENVENIDO AL SISTEMA DE CONSULTAS DEL ZOOLOGICO DE SAN DIEGO, CALIFORNIA\n Escoge la opcion que deses entre Consultas y Mantenimiento\n")
labelinst.place(x=90,y=170)

botonmante=Button(bg="green",fg="black",text="Mantenimiento",command=mantenimiento)
botonmante.place(x=100,y=250)

botonconsulta=Button(bg="green",fg="black",text="Consulta",command=consulta)
botonconsulta.place(x=400,y=250)
###########################
#####Definicion del MENU
###########################


barra=Menu(FrameInicio)
FrameInicio.config(menu=barra)
Archivo=Menu(barra)
barra.add_cascade(label="Archivo",menu=Archivo)
Archivo.add_command(label="Inicio")
Archivo.add_separator()
#Archivo.add_command(label="Mantenimiento",command=VerPerfil)
##Archivo.add_command(label="Consultas",command=ModPerfil)
Archivo.add_separator()
##Archivo.add_command(label="Salir", command=Cerrar)

Archivo2=Menu(barra)
barra.add_cascade(label="Ayuda",menu=Archivo2)
##Archivo2.add_command(label="Manual", command=Abrir)
Archivo2.add_separator()
Archivo2.add_command(label="Acerca de", command=acercade)



#############################################################################
FrameInicio.mainloop()
#############################################################################