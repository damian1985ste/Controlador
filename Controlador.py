#!/usr/bin/python
import time
import sys
sys.path.append('../')
from Vistas.Vistas import vistas
from Drivers.interfaz import interfazDR

per=interfazDR() # conexion a perifericos
v=vistas(per.disp) # conexion a vistas
class controlador:
	def __init__(self):
		L=cLectura()
		sel=1
		while True:
			btn = False
			rot = 0
			Nlin=L.mInicial(sel)
			while not btn and rot==0:
				btn = per.RE_btn_state()
				rot = per.RE_rot_state()
			if btn:
				if sel==1:
					btn1=False
					sel1=1
					while sel1!='X': #and not btn1:
						btn1=False
						rot1=0
						L.mDatosIngresar()
						while not btn1 and rot1==0:
						  btn1 = per.RE_btn_state()
						  #print(btn)
						  rot1 = per.RE_rot_state()
						## trabajar al enviar los datos de la base de datos las opciones posibles###
						if btn1:
						  if sel1==1:
							e1=DaRopc(e1)
						  elif sel1==2:
							e2=DaRopc(e2)
						  elif sel1==3:
							e3=DaRopc(e3)
						  elif sel1==4:
							e4=DaRopc(e4)
						  elif sel1==5:
							#Pantalla siguiente Lotes a identificar
							print('falta hacer pantalla')
						  elif sel11==6:
						    sel1='X'
						sel1=self.controlRE(sel1,rot1,6)
					print('prog.py - linea 122 -> Salgo del menu Comenzar a trabajar - Datos a Registrar')
					time.sleep(0.2)
					btn=False
				elif sel==2:
					#p.imp_menu('Descargar datos', 'Borrar registros','','Prueba 2')
					print('op 2')
				elif sel==3:
					#Codigo
					print('opcion 3')
				elif sel==4:
					# Apagar Ver de meter pantallita de apagado
					#print('Apagar')
					break
				else:
					#print('prog.py - linea 134 -> No es una opcion seleccionada') 
					break
			sel=self.controlRE(sel,rot,Nlineas )
''' ======PARA BORRAR=================				  
			if rot!=0:
				sel=sel+rot
				if sel==0:
					sel = 4
				elif sel == 5:
					sel = 1
===================================='''

	def controlRE(self, rot, seli, largo):		
		if rot!=0:
			sel=seli+rot
			if sel==0:
				sel = largo
			elif sel == largo+1:
				sel = 1
			return(sel)
	
	def DaRopc(opc):
		if opc==' ':
			opc='A'
		elif opc=='A':
			opc='M'
		elif opc=='M':
			opc=' '
		return(opc)

class cLectura:
	def __init__(self):
		v.pant_inicio()
		
	def mInicial(self, sel=1):
		'''Esta funcion realiza el trabajo necesario para presentar 
		pantalla el menu inicial'''
		wifi=True # consultar a base de datos configuracion
		BT=True # consultar a base de datos configuracion
		op=['Comenzar a Trabajar', 'Descargar Registros','Configurar','Apagar']
		v.imp_menu_op(op,sel,wifi,BT)
		return(len(op))
	
	def mDatosIngresar(self,sel=1):
		#print('no qnda todavia')
		title="Datos a registrar"
		cmd1,cmd2='Siguiente', 'Cancelar'
		e1,e2,e3,e4='A',' ','M','A' #borrar cuando se implemnete la consulta a base de datos
		lineas=[('Lectura',e1), ('Aftosa', e2), ('Vientre vacio',e3), ('Antiparasitario',e4)] # consultar las lineas de la base de datos
		#ARMAR EL CHEQUE CORRESPONDIENTE  A LA CANTIDAD DE LINEAS PARA PODER ARMAR VARIAS PANTALLAS DE 4 LINEAS
		# sel1,e1,e2,e3,e4=1,'A',' ','M','A'
		#('Datos a registrar', sel1, [('Lectura',e1), ('Aftosa', e2), ('Vientre vacio',e3), ('Antiparasitario',e4)], 'Siguiente', 'Cancelar')
		def imp_menu_sel(self,title,sel,lineas,cmd1,cmd2)
		#return(Nlineas) #numero de lineas para poder controlar sel
	#def mLotesIdentificar(self):
	
	#def mLecturaCaravanas(self):
