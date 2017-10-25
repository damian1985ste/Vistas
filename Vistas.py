#!/usr/bin/python
from inicio import inicio
from menu import menu

class vistas:
	def __init__(self, disp_con):
		self.disp = disp_con
		p=menu(self.disp)
		
	def pant_inicio(self):
		p.inicio(self.disp)
		
	def imp_menu_op(self,lineas,sel,wifi,BT):
		'''Esta funcion realiza la impresion en pantalla del menu de 
		acuerdo a lineas lista de lineas que son las opciones del menu y 
		se encontrara seleccionada la que indique el parametro sel con 
		valores de 1 a 4 (por defecto 1)'''
		p.imp_menu_op(self,lineas,sel,wifi,BT)
		
	def imp_menu_sel(self,title,sel,lineas,cmd1,cmd2):
		'''Esta funcion imprime la pantalla de seleccion a partir de los datos 
		que recibe como parametros: title el titulo de la pantalla, sel la opcion
		seleccionada, lineas una lista de 4 tuplas con el par parametro opcion'''
		p.imp_menu_sel(self,title,sel,lineas,cmd1,cmd2)
		
	def pant_lect_carav(self,nroCarText,nCaravana,cmd,sel,pesoTexto,peso,pais):
		'''Esta funcion imprime la pantalla de lectura de la caravana recibe el
		texto (Nro de caravana u en otro idioma), nCaravana (texto), cmd comando 
		del boton(Terminar), sel estado del boton, pesoTexto referecia al peso, 
		peso valor del peso y unidad y Pais del valor de la caravana'''
		p.pant_lect_carav(self,nroCarText,nCaravana,cmd,sel,pesoTexto,peso,pais)