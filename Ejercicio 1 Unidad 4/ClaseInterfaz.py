from tkinter import *
from tkinter import ttk, messagebox

class Interfaz(object):
	def __init__(self):
		self.__ventana = Tk()
		self.__ventana.title('Calculadora IPC')

		mainframe = Frame()
		mainframe.pack()
		ttk.Label(mainframe, text="Item").grid(row=0,column=0,padx=5,pady=5)
		ttk.Label(mainframe, text="Cantidad").grid(row=0,column=1,padx=5,pady=5)
		ttk.Label(mainframe, text="Precio año base").grid(row=0,column=2,padx=5,pady=5)
		ttk.Label(mainframe, text="Precio año actual").grid(row=0,column=3,padx=5,pady=5)
		ttk.Label(mainframe, text="Vestimenta").grid(row=1,column=0,padx=5,pady=5)
		ttk.Label(mainframe, text="Alimentos").grid(row=2,column=0,padx=5,pady=5)
		ttk.Label(mainframe, text="Educacion").grid(row=3,column=0,padx=5,pady=5)

		self.cantidadVesti = ttk.Entry(mainframe,background='')
		self.cantidadVesti.grid(row=1,column=1,padx=5,pady=5)

		self.precioBaseVesti = ttk.Entry(mainframe)
		self.precioBaseVesti.grid(row=1,column=2,padx=5,pady=5)

		self.precioActualVesti = ttk.Entry(mainframe)
		self.precioActualVesti.grid(row=1,column=3,padx=5,pady=5)

		self.cantidadAli = ttk.Entry(mainframe)
		self.cantidadAli.grid(row=2,column=1,padx=5,pady=5)

		self.precioBaseAli = ttk.Entry(mainframe)
		self.precioBaseAli.grid(row=2,column=2,padx=5,pady=5)

		self.precioActualAli = ttk.Entry(mainframe)
		self.precioActualAli.grid(row=2,column=3,padx=5,pady=5)

		self.cantidadEdu = ttk.Entry(mainframe)
		self.cantidadEdu.grid(row=3,column=1,padx=5,pady=5)

		self.precioBaseEdu = ttk.Entry(mainframe)
		self.precioBaseEdu.grid(row=3,column=2,padx=5,pady=5)

		self.precioActualEdu = ttk.Entry(mainframe)
		self.precioActualEdu.grid(row=3,column=3,padx=5,pady=5)

		self.botonframe = Frame()
		self.botonframe.pack()
		ttk.Button(self.botonframe,text='Calcular IPC',command=self.CalculaIPC).grid(row=1,column=1,padx=50,pady=10)
		ttk.Button(self.botonframe,text='Salir',command=self.__ventana.destroy).grid(row=1,column=2,padx=50,pady=10)
		ttk.Label(self.botonframe,text = 'IPC %').grid(row=2,column=0,padx=0,pady=10)
		

		self.__ventana.mainloop()

	def CalculaIPC(self):
		try:
			costoBase = float(self.cantidadVesti.get())*float(self.precioBaseVesti.get())+float(self.cantidadAli.get())*float(self.precioBaseAli.get())+float(self.cantidadEdu.get())*float(self.precioBaseEdu.get())
			costoActual = float(self.cantidadVesti.get())*float(self.precioActualVesti.get())+float(self.cantidadAli.get())*float(self.precioActualAli.get())+float(self.cantidadEdu.get())*float(self.precioActualEdu.get())
			total = int(costoActual/costoBase)*100
			self.ipcLabel = ttk.Label(self.botonframe,text=total)
			self.ipcLabel.grid(row=2,column=1,padx=0,pady=10)
		except ValueError:
			messagebox.showerror(title='Error', message='Debe ingresar un valor en todas las casillas')
