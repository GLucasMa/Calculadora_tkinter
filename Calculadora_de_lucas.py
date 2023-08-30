# Como funciona global? def funcion y nombramos global
# como funciona bind? example: self.bind("<Enter>", self.on_enter)    == Entrada del mouse 
# Entry es caja de texto??
# root es lo mismo que ventana = Tk()? con root. se pueden realizar mas cosas?
#frame.pack()? empaquetamiento del frame

from tkinter import Button, Tk, Frame,Entry,END

ventana = Tk()
ventana.geometry('600x350')

#bg = background 
ventana.config(bg= "white")


ventana.resizable(1, 1)
ventana.title('Calculadora de lucas')

class HoverButton(Button):
	def __init__(self, master, **kw):
		Button.__init__(self,master= master,**kw)
		self.defaultBackground = self["background"]
		self.bind("<Enter>", self.on_enter)
		self.bind("<Leave>", self.on_leave)

	def on_enter(self, e):
		self["background"] = self["activebackground"]

	def on_leave(self, e):
		self["background"] = self.defaultBackground

#Creamos una variable frame nueva en donde guardaremos un widget Frame (esteos seran los bordes) 
#al cual le pasamos la variable ventana creada anteriormente, y otros parametros como el fondo y el relieve
frame = Frame(ventana, bg ='#353a3b', relief = "raised")
#El método grid nos permite posicionar los widgets en una celda en especifico,
#indicamos la celda usando el índice de fila y columna correspondiente y lo usamos con la variable frame que
#acabamos de crear
frame.grid(column=0, row=0, padx=2, pady=6)

#A la clase Entry (Esta sera la caja donde se muestra el texto) 
#la cual es una caja de texto le pasamos lo que teniamos en la variable frame 
#ademas le indicamos el fondo, ancho, relieve, fuente y justificado a que lado
Resultado = Entry(frame,bg='#418ea4', width=36, relief='groove', font = 'BookmanOldStyle 22',justify='right')
Resultado.grid(columnspan=6 ,row=0, pady=2,padx=2, ipadx=1, ipady=1) 


#place lo usamos para poder darle altura a Entry
""" Resultado.place(x = 5,
        y = 5,
        width=470,
        height=90) """

# i será nuestra memoria. La función guarda el dato y lo coloca con la cantidad de espacios de i
i=0
def obtener(dato):
	global i
	i+=1
	Resultado.insert(i, dato)
	
def operacion():
	global i
	ecuacion = Resultado.get()
	if i !=0:		
		try:
			result = str(eval(ecuacion))
			Resultado.delete(0,END)
			Resultado.insert(0,result)
			longitud = len(result)
			i = longitud
		except:
			result = 'Syntax Error'
			Resultado.delete(0,END)
			Resultado.insert(0,result)
	else:
		pass

def borrar_uno(): #???????
	global i 
	if i==-1:
		pass
	else:
		Resultado.delete(i,last =None)
		i-=1

def borrar_todo():
	Resultado.delete(0, END)	
	#i=0



#fila 1
Button7 = HoverButton(frame, text= "7", borderwidth=10, height=2, width=9, 
	font= ('Comic sens MC',12,'bold'),relief = "raised", activebackground="#999AB8", bg ='#999AB8',  
	anchor="center", command=lambda: obtener(7))  
Button7.grid( column= 0 ,row=1, pady=1,padx=1)
Button8 = HoverButton(frame, text= "8", borderwidth=10, height=2, width=9, 
	font= ('Comic sens MC',12,'bold'),  relief = "raised", activebackground="#999AB8",bg ='#999AB8', 
	anchor="center",command=lambda: obtener(8))  
Button8.grid(column =1 , row=1, pady=1,padx=1)
Button9= HoverButton(frame, text= "9", borderwidth=10, height=2, width=9,
	font= ('Comic sens MC',12,'bold'),  relief = "raised", activebackground="#999AB8", bg ='#999AB8', 
	anchor="center",command=lambda: obtener(9))  
Button9.grid(column =2, row=1, pady=1,padx=1)


Button_borrar = HoverButton(frame, text= "⌫",borderwidth=10, height=2, width=9,
	font= ('Comic sens MC',12,'bold'),  relief = "raised", activebackground="#ba0f0f", 
	bg='#ba0f0f',  anchor="center",command=lambda: borrar_uno())  
Button_borrar.grid(column =3, row=1, pady=1,padx=1)
ButtonCE = HoverButton(frame, text= "CE",borderwidth=10, height=2, width=9,
	font= ('Comic sens MC',12,'bold'),  relief = "raised", activebackground="#ba0f0f", 
	bg='#ba0f0f',  anchor="center",command=lambda: borrar_todo())  
ButtonCE.grid(column =4, row=1, pady=1,padx=1)

#fila 2
Button4 = HoverButton(frame, text= "4", borderwidth=10, height=2, width=9, 
	font= ('Comic sens MC',12,'bold'),relief = "raised", activebackground="#999AB8", bg ='#999AB8',  
	anchor="center", command=lambda: obtener(4))  
Button4.grid( column= 0 ,row=2, pady=1,padx=1)
Button5 = HoverButton(frame, text= "5", borderwidth=10, height=2, width=9, 
	font= ('Comic sens MC',12,'bold'),relief = "raised", activebackground="#999AB8", bg ='#999AB8',  
	anchor="center", command=lambda: obtener(5))  
Button5.grid( column= 1,row=2, pady=1,padx=1)
Button6 = HoverButton(frame, text= "6", borderwidth=10, height=2, width=9, 
	font= ('Comic sens MC',12,'bold'),relief = "raised", activebackground="#999AB8", bg ='#999AB8',  
	anchor="center", command=lambda: obtener(6))  
Button6.grid( column= 2,row=2, pady=1,padx=1)

Buttonmen = HoverButton(frame, text= "-",borderwidth=10, height=2, width=9,
	font= ('Comic sens MC',12,'bold'),  relief = "raised", activebackground="#999AB8", bg ='#999AB8',
	anchor="center",command=lambda: obtener('-'))  
Buttonmen.grid(column =3, row=2, pady=1,padx=1)
Buttonpor = HoverButton(frame, text= "*",borderwidth=10, height=2, width=9,
	font= ('Comic sens MC',12,'bold'),  relief = "raised", activebackground="#999AB8", bg ='#999AB8',
	anchor="center",command=lambda: obtener('*'))  
Buttonpor.grid(column =4, row=2, pady=1,padx=1)


#fila 3
Button1 = HoverButton(frame, text= "1", borderwidth=10, height=2, width=9, 
	font= ('Comic sens MC',12,'bold'),relief = "raised", activebackground="#999AB8", bg ='#999AB8',  
	anchor="center", command=lambda: obtener(1))  
Button1.grid( column= 0 ,row=3, pady=1,padx=1)
Button2 = HoverButton(frame, text= "2", borderwidth=10, height=2, width=9, 
	font= ('Comic sens MC',12,'bold'),relief = "raised", activebackground="#999AB8", bg ='#999AB8',  
	anchor="center", command=lambda: obtener(2))  
Button2.grid( column= 1,row=3, pady=1,padx=1)
Button3 = HoverButton(frame, text= "3", borderwidth=10, height=2, width=9, 
	font= ('Comic sens MC',12,'bold'),relief = "raised", activebackground="#999AB8", bg ='#999AB8',  
	anchor="center", command=lambda: obtener(3))  
Button3.grid( column= 2,row=3, pady=1,padx=1)

Buttonmas = HoverButton(frame, text= "+",borderwidth=10, height=2, width=9,
	font= ('Comic sens MC',12,'bold'),  relief = "raised", activebackground="#999AB8", bg ='#999AB8',
	anchor="center",command=lambda: obtener('+'))  
Buttonmas.grid(column =3, row=3, pady=1,padx=1)
Buttondiv = HoverButton(frame, text= "÷",borderwidth=10, height=2, width=9,
	font= ('Comic sens MC',12,'bold'),  relief = "raised", activebackground="#999AB8", bg ='#999AB8',
	anchor="center",command=lambda: obtener('/'))  
Buttondiv.grid(column =4, row=3, pady=1,padx=1)



#fila 4
Button0 = HoverButton(frame, text= "0", borderwidth=10, height=2, width=21, 
	font= ('Comic sens MC',12,'bold'),relief = "raised", activebackground="#999AB8", bg ='#999AB8',  
	anchor="center", command=lambda: obtener(0))  
Button0.grid( column= 0 ,columnspan=2, row=5, pady=1,padx=1)

Buttonpoint= HoverButton(frame, text= ".", borderwidth=10, height=2, width=9, 
	font= ('Comic sens MC',12,'bold'),relief = "raised", activebackground="#999AB8", bg ='#999AB8',  
	anchor="center", command=lambda: obtener('.'))  
Buttonpoint.grid( column= 2 ,row=5, pady=1,padx=1)

Buttonequal= HoverButton(frame, text= "=", borderwidth=10, height=2, width=21, 
	font= ('Comic sens MC',12,'bold'),relief = "raised", activebackground="#999AB8", bg ='#999AB8',  
	anchor="center", command=lambda: operacion())  
Buttonequal.grid( column= 3 ,columnspan=2, row=5, pady=1,padx=1)



ventana.mainloop()