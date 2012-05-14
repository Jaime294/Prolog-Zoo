#######################################################################
#TAREA PROGRAMADA 2####################################################
#######################################################################
###Luis Diego Conejo Mora##Amed Espinoza Castro##Isaac Lopez Delgado###
#######################################################################



#########################
#### Modulos Importados
#########################

from Tkinter import*
import tkMessageBox as box
from string import*
from prolog import Prolog
import ttk


########################
#### Definicion del Frame
########################
FrameInicio=Tk()
FrameInicio.geometry("597x450")
FrameInicio.title("Zoologico de San Diego, California // Consulta de Animales")

#Definicion de la variable donde se guardara la base de conocimientos
baseconocimientos=Prolog()

#Funcion que devuelve un frame con un acerca de la aplicacion
def acercade():
    filewin = Toplevel(FrameInicio)
    info = Label(filewin, text="Programacion de sistema de consultas",font=20)
    info1 = Label(filewin, text="Zoologico de San Diego, California")
    info2 = Label(filewin, text="Un sistema de consultas de animales hecha con TKinter, Python y un wrapper, Pyswip")
    info3 = Label(filewin, text="Disenador: Luis Diego Conejo Mora, Amed Espinoza Castro, Isaac Lopez Delgado")
    info4 = Label(filewin, text="Programada por: Luis Diego Conejo Mora, Amed Espinoza Castro, Isaac Lopez Delgado")
    info5 = Label(filewin, text="Pyswip, wrapper de conexion con Prolog")
    info6 = Label(filewin, text="Copyright 05/2012")
    info.pack()
    info2.pack()
    info3.pack()
    info4.pack()
    info5.pack()
    info6.pack()

###############################
#### Funcion de Mantenimiento
###############################
def mantenimiento():
    #Definicion del canvas y las variables y labels
    fondo=Canvas(FrameInicio,width=597,height=309,bg="white")
    fondo.place(x=0,y=141)
    
    #Definicion de la variable Raza, con lectura de un archivo txt que contiene
    #el nombre de todos los animales del Zoologico // Implementa Combobox
    varraza=StringVar()
    a=open("animal.txt","r")
    datos=a.read()
    lista1=str.split(datos,"\r\n")
    listaraza=ttk.Combobox(state="readonly",values=lista1,textvariable=varraza)
    listaraza.place(x=200,y=150)
    varraza.set("Elija una raza")
    labelraza=Label(bg='white',fg='black',text="Raza:")
    labelraza.place(x=90,y=150)
    labelind1=Label(bg='white',fg="red",text="Elija una raza  (Estan subdivididas en Anfibios, Aves, Mamiferos, Reptiles e Insectos)",font=("Arial",8))
    labelind1.place(x=90,y=170)
    
    #Definicion de la variable Edad, con una iteracion de numeros del 0 al 100
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

	#Definicion de la variable Genero
    vargenero=StringVar()
    lista3=["Macho","Hembra","Asexual"]
    listagenero=ttk.Combobox(state="readonly",values=lista3,textvariable=vargenero)
    listagenero.place(x=200,y=230)
    vargenero.set("Elija un genero")
    labelgenero=Label(bg='white',fg='black',text="Genero:")
    labelgenero.place(x=90,y=230)
    labelind3=Label(bg='white',fg="red",text="Elija el genero del animal",font=("Arial",8))
    labelind3.place(x=90,y=250)

	#Definicion de la variable Nombre // Implementa Entry
    varnombre=StringVar()
    entrynombre=Entry(bg='white',fg='black',width=30,textvariable=varnombre)
    entrynombre.place(x=200,y=270)
    labelnombre=Label(bg='white',fg='black',text="Nombre:")
    labelnombre.place(x=90,y=270)
    labelind4=Label(bg='white',fg="red",text="Escriba el nombre del animal",font=("Arial",8))
    labelind4.place(x=90,y=290)

	#Definicion de la variable Ecosistema // IMplementa COmbobox
    vareco=StringVar()
    b=open("ecosistema.txt","r")
    datos2=b.read()
    lista4=str.split(datos2,"\r\n")
    listaeco=ttk.Combobox(state="readonly",values=lista4,textvariable=vareco)
    listaeco.place(x=200,y=310)
    vareco.set("Elija un ecosistema")
    labeleco=Label(bg='white',fg='black',text="Ecosistema:")
    labeleco.place(x=90,y=310)
    labelind5=Label(bg='white',fg="red",text="Elija el ecosistema original del animal",font=("Arial",8))
    labelind5.place(x=90,y=330)

	#Definicion de la variable Comida // IMplementa Entry
    varcomida=StringVar()
    entrycomida=Entry(bg='white',fg='black',width=30,textvariable=varcomida)
    entrycomida.place(x=200,y=350)
    labelcomida=Label(bg='white',fg='black',text="Comida:")
    labelcomida.place(x=90,y=350)
    labelind6=Label(bg='white',fg="red",text="Escriba la comida favorita del animal",font=("Arial",8))
    labelind6.place(x=90,y=370)
	
	#Definicion de un boton que abra la parte de consultas
    botonconsulta=Button(bg="green",fg="black",text="Consulta",command=consulta)
    botonconsulta.place(x=450,y=250)

	#Definicion de una sub-funcion que agrega el animal a la base de conocimientos
    def agregar():
		#COmprueba que todos los campos tengan datos pertinentes
		if ((varraza.get()!="" and varraza.get()!="Elija una raza")and (vargenero.get()!="" and vargenero.get()!="Elija un genero")and(varedad.get()!="" and varedad.get()!="Elija una edad")and varnombre.get()!="" and varcomida.get()!="" and (vareco.get()!="" and vareco.get()!="Elija un ecosistema")):
			#Hace el ingreso de los datos a la base de conocimientos
			baseconocimientos.assertz("animal("+lower(varraza.get())+","+lower(varedad.get())+","+lower(vargenero.get())+","+lower(varnombre.get())+","+lower(vareco.get())+","+lower(varcomida.get())+")")
			#Pregunta si desea agregar otro animal o sino lo lleva al inicio
			resp=box.askyesno("Animal agregado","El animal ya fue agregado a la base de conocimientos\nDesea agregar otro?")
			if resp==True:
				varraza.set("Elija una raza")
				varedad.set("Elija una edad")
				vareco.set("")
				varcomida.set("")
				varnombre.set("")
				vargenero.set("Elija un genero")
			else:
				fondo=Canvas(FrameInicio,width=597,height=309,bg="white")
				fondo.place(x=0,y=141)
				labelinst=Label(bg="white",text="BIENVENIDO AL SISTEMA DE CONSULTAS DEL ZOOLOGICO DE SAN DIEGO, CALIFORNIA\n Escoge la opcion que deses entre Consultas y Mantenimiento\n")
				labelinst.place(x=30,y=170)

				botonmante=Button(bg="green",fg="black",text="Mantenimiento",command=mantenimiento)
				botonmante.place(x=100,y=250)

				botonconsulta=Button(bg="green",fg="black",text="Consulta",command=consulta)
				botonconsulta.place(x=400,y=250)
		else:
			box.showwarning("Animal erroneo","EL animal no puede ser agregado porque faltan datos")
    #Definicion de la sub-funcion de borrar, que devuelve los combobox y entrys a vacios
    def borrar():
        varraza.set("Elija una raza")
        varedad.set("Elija una edad")
        vareco.set("Elija un ecosistema")
        varcomida.set("")
        varnombre.set("")
        vargenero.set("Elija un genero")
    #Definicion de los botones que implementan las sub-funciones anteriores
    botonagregar=Button(bg="green",fg="black",text="Agregar Animal",command=agregar)
    botonagregar.place(x=200,y=400)

    botonborrar=Button(bg="green",fg="black",text="Borrar datos",command=borrar)
    botonborrar.place(x=350,y=400)

############################
#### Definicion de Consulta
############################
def consulta():
	#Define el fondo y todas las variables necesarias
    fondo=Canvas(FrameInicio,width=597,height=309,bg="white")
    fondo.place(x=0,y=141)
    
	#Definicion de la variable Raza, con lectura de un archivo txt que contiene
    #el nombre de todos los animales del Zoologico // Implementa Combobox
    varraza=StringVar()
    a=open("animal.txt","r")
    datos=a.read()
    lista1=str.split(datos,"\r\n")
    listaraza=ttk.Combobox(state="readonly",values=lista1,textvariable=varraza)
    listaraza.place(x=200,y=150)
    varraza.set("")
    labelraza=Label(bg='white',fg='black',text="Raza:")
    labelraza.place(x=90,y=150)
    labelind1=Label(bg='white',fg="red",text="Elija una raza  (Estan subdivididas en Anfibios, Aves, Mamiferos, Reptiles e Insectos)",font=("Arial",8))
    labelind1.place(x=90,y=170)
    
    #Definicion de la variable Edad, con una iteracion de numeros del 0 al 100
    varedad=StringVar()
    lista2=[""]
    for i in range(0,100):
        lista2.append(i)
    listaedad=ttk.Combobox(state="readonly",values=lista2,textvariable=varedad)
    listaedad.place(x=200,y=190)
    varedad.set("")
    labeledad=Label(bg='white',fg='black',text="Edad:")
    labeledad.place(x=90,y=190)
    labelind2=Label(bg='white',fg="red",text="Elija la edad del animal",font=("Arial",8))
    labelind2.place(x=90,y=210)

	#Definicion de la variable genero // Implementa combobox
    vargenero=StringVar()
    lista3=["","Macho","Hembra","Asexual"]
    listagenero=ttk.Combobox(state="readonly",values=lista3,textvariable=vargenero)
    listagenero.place(x=200,y=230)
    vargenero.set("")
    labelgenero=Label(bg='white',fg='black',text="Genero:")
    labelgenero.place(x=90,y=230)
    labelind3=Label(bg='white',fg="red",text="Elija el genero del animal",font=("Arial",8))
    labelind3.place(x=90,y=250)

	#Definicion de la variable nombre // IMplementa entry
    varnombre=StringVar()
    entrynombre=Entry(bg='white',fg='black',width=30,textvariable=varnombre)
    entrynombre.place(x=200,y=270)
    labelnombre=Label(bg='white',fg='black',text="Nombre:")
    labelnombre.place(x=90,y=270)
    labelind4=Label(bg='white',fg="red",text="Escriba el nombre del animal",font=("Arial",8))
    labelind4.place(x=90,y=290)

	#Definicion de la variable Ecosistema // IMplementa lectura de archivos y combobox
    vareco=StringVar()
    b=open("ecosistema.txt","r")
    datos2=b.read()
    lista4=str.split(datos2,"\n")
    listaeco=ttk.Combobox(state="readonly",values=lista4,textvariable=vareco)
    listaeco.place(x=200,y=310)
    vareco.set("")
    labeleco=Label(bg='white',fg='black',text="Ecosistema:")
    labeleco.place(x=90,y=310)
    labelind5=Label(bg='white',fg="red",text="Elija el ecosistema original del animal",font=("Arial",8))
    labelind5.place(x=90,y=330)

	#Definicion de la variable COmida // IMplementa entry
    varcomida=StringVar()
    entrycomida=Entry(bg='white',fg='black',width=30,textvariable=varcomida)
    entrycomida.place(x=200,y=350)
    labelcomida=Label(bg='white',fg='black',text="Comida:")
    labelcomida.place(x=90,y=350)
    labelind6=Label(bg='white',fg="red",text="Escriba la comida favorita del animal",font=("Arial",8))
    labelind6.place(x=90,y=370)

    botonmante=Button(bg="green",fg="black",text="Mantenimiento",command=mantenimiento)
    botonmante.place(x=450,y=250)
    
	#Definicion de una sub-funcion que devuelve todos los entrys y combobox a vacios
    def borrar():
        varraza.set("")
        varedad.set("")
        vareco.set("")
        varcomida.set("")
        varnombre.set("")
        vargenero.set("")    
    #Definicion del boton que implementa la sub-funcion borrar
    botonborrar=Button(bg="green",fg="black",text="Borrar datos",command=borrar)
    botonborrar.place(x=350,y=400)
    
    #Definicion de la sub-funcion consultar que realiza la consulta con los datos ingresados
    def consultar():
		#Se definen tres variables, donde en var entran los datos que no fueron declarados
		#en var2 entran los campos que no fueron declarados, y en cons entran
		#los valores que SI fueron declarados.
		var=[]
		var2=[]
		cons=[]
		
		#UNa serie de ifs y elses, donde valida si el valor es una variable, o una constante
		if (varraza.get()=="" or varraza.get()=="Elija una raza"):
			raza="X"
			var+=[raza]
			var2+=["Raza"]
		else:
			raza=lower(varraza.get())
			cons+=[["Raza",raza]]
		#UNa serie de ifs y elses, donde valida si el valor es una variable, o una constante
		if varedad.get()=="" or varedad.get()=="Elija una edad":
			edad="Y"
			var+=[edad]
			var2+=["Edad"]
		else:
			edad=varedad.get()
			cons+=[["Edad",edad]]
		#UNa serie de ifs y elses, donde valida si el valor es una variable, o una constante	
		if vargenero.get()=="" or vargenero.get()=="Elija un genero":
			genero="Z"
			var+=[genero]
			var2+=["Genero"]
		else:
			genero=lower(vargenero.get())
			cons+=[["Genero",genero]]
		#UNa serie de ifs y elses, donde valida si el valor es una variable, o una constante
		if vareco.get()=="" or vareco.get()=="Elija un ecosistema":
			eco="A"
			var+=[eco]
			var2+=["Ecosistema"]
		else:
			eco=lower(vareco.get())
			cons+=[["Ecosistema",eco]]
		#UNa serie de ifs y elses, donde valida si el valor es una variable, o una constante
		if varnombre.get()=="":
			nbr="B"
			var+=[nbr]
			var2+=["Nombre"]
		else:
			nbr=lower(varnombre.get())
			cons+=[["Nombre",nbr]]
		#UNa serie de ifs y elses, donde valida si el valor es una variable, o una constante
		if varcomida.get()=="":
			com="C"
			var+=[com]
			var2+=["Comida"]
		else:
			com=lower(varcomida.get())
			cons+=[["Comida",com]]
		
		#Define la variable flag que declara si se logro realizar la consulta o no
		flag=False
		try:
			#Try que valida si se logra realizar la consulta con los datos ingresados
			consulta=list(baseconocimientos.query("animal("+raza+","+edad+","+genero+","+nbr+","+eco+","+com+")"))
			
			if consulta!=[]:
				flag=True
		except:
			#Entra aca si la consulta no se pudo realizar
			box.showwarning("NO existe","La consulta que intenta realizar no tiene resultados")
			pass
		
		#ENtra aca si la consulta se realizo, pero no hubo ningun resultado
		if not flag:
			box.showwarning("NO existe","La consulta que intenta realizar no tiene resultados")
		else:	
			#Define una nueva ventana donde sera agregado las respuestas de la consulta
			est=Toplevel() 
			est.geometry("800x450")
			est.title("Zoologico de San Diego, California // Consulta de Animales")
			fondor=Canvas(est,width=800,height=450,bg="white")
			fondor.place(x=0,y=0)
			photo = PhotoImage(file="header.GIF")
			labelimagen1=Label(est,image=photo)
			labelimagen1.place(x=0,y=0)
			x2=10
			y2=150
			
			#Aca se escribe las constantes que fueron agregadas para realizar la consulta
			labelinf=Label(est,bg="white",text="Se consultaron los siguientes datos: ")
			labelinf.place(x=x2,y=y2)
			y2+=15
			
			#Se itera en la variable cons para imprimir las constantes
			for i in cons:
				labelinf2=Label(est,bg="white",text=i[0]+": "+i[1],font=("Helvetica", 12))
				labelinf2.place(x=x2,y=y2)
				x2+=200
			x1=10
			y1=240
			x3=110
			y3=200
			#Se pone una referencia a los campos de las variables
			for t in var2:
				labelvar2=Label(est,bg="white",text=t)
				labelvar2.place(x=x3,y=y3)
				x3+=100
			#Se itera sobre la lista var, y la lista consulta, para mostrar las respuestas de la consulta
			for i in range(0,len(consulta)):
				labelcons=Label(est,bg="white",text="Animal: ")
				labelcons.place(x=x1,y=y1)
				x1+=100
				for j in range(0,len(var)):
					labelcons=Label(est,bg="white",text=consulta[i][var[j]])
					labelcons.place(x=x1,y=y1)
					x1+=100
				x1=10
				y1+=20
			
			est.mainloop()
	#Boton de consulta que usa la sub-funcion anterior
    botonconsultar=Button(bg="green",fg="black",text="Consultar",command=consultar)
    botonconsultar.place(x=200,y=400)	
	
#Funcion del menu que cierra la aplicacion	
def Cerrar():
	FrameInicio.destroy()	
	
#Funcion del menu que devuelve al inicio
def Inicio():
	fondo=Canvas(FrameInicio,width=597,height=309,bg="white")
	fondo.place(x=0,y=141)
	labelinst=Label(bg="white",text="BIENVENIDO AL SISTEMA DE CONSULTAS DEL ZOOLOGICO DE SAN DIEGO, CALIFORNIA\n Escoge la opcion que deses entre Consultas y Mantenimiento\n")
	labelinst.place(x=30,y=170)

	botonmante=Button(bg="green",fg="black",text="Mantenimiento",command=mantenimiento)
	botonmante.place(x=100,y=250)

	botonconsulta=Button(bg="green",fg="black",text="Consulta",command=consulta)
	botonconsulta.place(x=400,y=250)
   
############################
#### Definicion del INICIO
############################ 
fondor=Canvas(FrameInicio,width=597,height=450,bg="white")
fondor.place(x=0,y=0)
photo = PhotoImage(file="header.GIF")
labelimagen=Label(FrameInicio,image=photo)
labelimagen.place(x=0,y=0)

labelinst=Label(bg="white",text="BIENVENIDO AL SISTEMA DE CONSULTAS DEL ZOOLOGICO DE SAN DIEGO, CALIFORNIA\n Escoge la opcion que deses entre Consultas y Mantenimiento\n")
labelinst.place(x=30,y=170)

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
Archivo.add_command(label="Inicio",command=Inicio)
Archivo.add_separator()
Archivo.add_command(label="Mantenimiento",command=mantenimiento)
Archivo.add_command(label="Consultas",command=consulta)
Archivo.add_separator()
Archivo.add_command(label="Salir", command=Cerrar)

Archivo2=Menu(barra)
barra.add_cascade(label="Ayuda",menu=Archivo2)
##Archivo2.add_command(label="Manual", command=Abrir)
Archivo2.add_separator()
Archivo2.add_command(label="Acerca de", command=acercade)



#############################################################################
FrameInicio.mainloop()
#############################################################################
