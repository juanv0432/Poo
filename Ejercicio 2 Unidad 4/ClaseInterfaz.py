from tkinter import *
from tkinter import ttk, messagebox

class Interfaz(object):
	def __init__(self):
		self.__ventana = Tk()
		self.__ventana.title('Calculadora IVA')

		self.__varopcion=IntVar()
		self.__IVA=StringVar()
		self.__PrecioConIVA=StringVar()
	

		frameSup = Frame()
		frameSup.config(background='#DAE8FC',relief="solid",width='300')
		Label(frameSup,text='Cálculo de IVA',bg='#DAE8FC').grid(row=1,column=1,padx=30,pady=20)
		frameSup.pack()


		frameMid = Frame()
		ttk.Label(frameMid,text='Precio sin IVA').grid(row=0,column=0,padx=10,pady=10,sticky=W)
		ttk.Radiobutton(frameMid,text='IVA 21%',variable=self.__varopcion,value=1).grid(row=1,column=0,padx=10,pady=10,sticky=W)
		ttk.Radiobutton(frameMid,text='IVA 10.5%',variable=self.__varopcion,value=2).grid(row=2,column=0,padx=10,pady=10,sticky=W)
		ttk.Label(frameMid,text='IVA').grid(row=3,column=0,padx=10,pady=10,sticky=W)
		ttk.Label(frameMid,text='Precio con IVA').grid(row=4,column=0,padx=10,pady=10,sticky=W)

		self.PrecioBase = Entry(frameMid,relief="solid")
		self.PrecioBase.grid(row=0,column=1,padx=10,pady=10)
		Entry(frameMid,relief="solid",textvariable=self.__IVA, state='disabled').grid(row=3,column=1,padx=10,pady=10)
		Entry(frameMid,relief="solid",textvariable=self.__PrecioConIVA, state='disabled').grid(row=4,column=1,padx=10,pady=10)
		frameMid.pack()

		frameInf = Frame()
		Button(frameInf,text='Calcular', bg="#DAE8FC", relief="ridge",command=self.Calcula).grid(row=0,column=0,padx=10,pady=10)
		Button(frameInf,text='Salir',bg="#F8CECC", relief="ridge",command=self.__ventana.destroy).grid(row=0,column=1,padx=10,pady=10)
		frameInf.pack()

		self.__ventana.mainloop()

	def Calcula(self):
		total=0
		try:
			if self.__varopcion.get() == 1:
				total = float(self.PrecioBase.get())*21*100
				self.__IVA.set('21%')
				self.__PrecioConIVA.set(total)
			elif self.__varopcion.get() == 2:
				total = float(self.PrecioBase.get())*10.5*100
				self.__IVA.set('10.5%')
				self.__PrecioConIVA.set(total)
		except ValueError:
			messagebox.showerror(title='Error', message='Debe ingresar un valor en la casilla Precio sin IVA')

			
