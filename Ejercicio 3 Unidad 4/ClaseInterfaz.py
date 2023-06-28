from tkinter import *
from urllib.request import urlopen
import json

class Interfaz(object):
	def __init__(self):
		self.__ventana = Tk()
		self.__ventana.title('Conversor Moneda')

		self.frameMid = Frame()
		self.CantidadDolares = Entry(self.frameMid)
		self.CantidadDolares.grid(row=0,column=0,padx=10,pady=10)
		Label(self.frameMid,text='dólares').grid(row=0,column=1,padx=10,pady=10,sticky=E)
		Label(self.frameMid,text='es equivalente a ').grid(row=1,column=0,padx=10,pady=10)
		Label(self.frameMid,text='pesos').grid(row=1,column=2,padx=10,pady=10)
		self.frameMid.pack()

		frameInf = Frame()
		Button(frameInf,text='Calcular',command=self.Calcular).grid(row=1,column=1,padx=10,pady=10)
		frameInf.pack()

		self.__ventana.mainloop()
			
	def ObtenerValorDolar(self):
		url = "https://www.dolarsi.com/api/api.php?type=dolar"
		response = urlopen(url)
		data = json.loads(response.read())
		precioDolar = 0
		for i in data:
			casa = i['casa']
			if casa['nombre'] == 'Blue':
				precioDolar = casa['compra'].replace(',', '.')
		return precioDolar

	def Calcular(self):
		try:
			total = int(self.CantidadDolares.get())*float(self.ObtenerValorDolar())
			Label(self.frameMid,text=total).grid(row=1,column=1,padx=10,pady=10)
		except ValueError:
			pass