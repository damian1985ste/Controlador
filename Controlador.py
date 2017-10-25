#!/usr/bin/python
from Vistas.Vistas import vistas
from Drivers.interfaz import interfazDR

per=interfazDR() # conexion a perifericos
v=vistas(p.disp) # conexion a vistas
class controlador:
	def __init__(self):
		L=cLectura()
		sel=1
		while True:
			btn = False
			rot = 0
			L.mInicial(sel)
			while not btn and rot==0:
				btn = per.RE_btn_state()
				rot = per.RE_rot_state()
				if btn:
					if sel==1:
						btn1=False
						while sel1!='X': #and not btn1:
							btn1=False
							rot1=0
							L.mDatosIngresar()
							###======== FALTA EL CODIGO
					elif sel==2:
						#p.imp_menu('Descargar datos', 'Borrar registros','','Prueba 2')
					elif sel==3:
						#Codigo
						print('opcion 3')
					elif sel==4:
						# Apagar Ver de meter pantallita de apagado
						break
					else:
						print('prog.py - linea 134 -> No es una opcion seleccionada') 
						break
					  
				if rot!=0:
					sel=sel+rot
					if sel==0:
						sel = 4
					elif sel == 5:
						sel = 1
					
	
class cLectura:
	def __init__(self):
	
	def mInicial(self, sel=1):
		'''Esta funcion realiza el trabajo necesario para presentar 
		pantalla el menu inicial'''
		wifi=True # consultar a base de datos configuración
		BT=True # consultar a base de datos configuración
		op=['Comenzar a Trabajar', 'Descargar Registros','Configurar','Apagar']
		v.imp_menu_op(op,sel,wifi,BT)
	
	def mDatosIngresar(self):
		# sel1,e1,e2,e3,e4=1,'A',' ','M','A'
		#('Datos a registrar', sel1, [('Lectura',e1), ('Aftosa', e2), ('Vientre vacio',e3), ('Antiparasitario',e4)], 'Siguiente', 'Cancelar')
	def mLotesIdentificar(self):
	
	def mLecturaCaravanas(self):