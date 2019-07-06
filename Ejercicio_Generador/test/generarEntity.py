#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import random
import os
nombresM = ["Daniel","Alfonso","Jhonathan","David","Federico","German","Alejandro","Pedro","Mauricio","Santiago","Lionel","Cristian","Jose","Sebastian","Juan","Gustavo","Alfredo","Bryan","Bayron","Jairo","Jorge","Hernando","Fernando","Luis"]

nombresF = ["Esmeralda","Luisa","Angela","Alexa","Susana","Lucia","Angela","Maria","Ana","Paula","Priscila","Valentina","Natalie","Monica","Ximena","Catalina","Ivanna","Sofia","Andrea","Veronica"]

apellido =["Vargas","Rojas","Ortiz","DeLaRua","MontFerrer","Pitana","Dybala","Hernandez","Rodriguez","Balaguera","Daza","Pertuz","Perez","Baquero","Isla","Vidal","Cardenas","Cadena", "Caminero","Escudero","Torres","Pinto","Vergara","Lopez","Almonacid","Rubio","Thompson","DeLigt","Garces","Benitez","Daronco","Sarri","Scarpetta","Almaguer","Garrido","Espinel","Cardozo","Garcia","Fornals","Puig","Schmidt","Malaver","Parra","Buscalia","Nieto","Molina","Pardo","Polanco","Zuniga"]


def actividad():
	act = ["Monitor","Curso GNU","Ayudante","Secretario","Hackathon","Asesoria Linux"]

	return act[random.randint(0,len(act)-1)]


def codigo():
	x = ["005","007","015","020","025"]
	year = random.randint(2011,2018)
	semester = random.randint(1,2)
	career = x[random.randint(0,len(x)-1)]
	idNumber = random.randint(0,999)

	if idNumber < 10:
		iden = "00"+str(idNumber)
	elif idNumber < 100:
		iden = "0"+str(idNumber)
	else:
		iden = str(idNumber)

	return str(year)+str(semester)+career+iden

def nota():
	return str(random.randint(40,50))


def generarNombres(n):
	listaNombres = []
	for i in range(0,n):
		gender = random.randint(0,1)
		primAp = apellido[random.randint(0,len(apellido)-1)]
		segAp = apellido[random.randint(0,len(apellido)-1)]
		if gender == 0:
			p = random.randint(0,len(nombresM)-1)			
			x = nombresM[p] + " " + primAp + " " + segAp
		else:
			p = random.randint(0,len(nombresF)-1)
			x = nombresF[p] + " " + primAp + " " + segAp

		listaNombres.append(x)
	return listaNombres

tam = 20
nombrecillos = generarNombres(tam)
#print(nombrecillos)


archivo = open( "person.ent","w")
num = 1
for elem in nombrecillos:
        code = codigo();
        k = "Iden"+str(num);
        archivo.write("certificado "+k+ " {\n")
        archivo.write("  \""+elem+"\"\n")
        archivo.write("  "+code+"\n")
        archivo.write("  "+nota()+"\n")
        activNums = random.randint(1,5)

        for i in range(0,activNums):
        	archivo.write("  \""+actividad()+"\"\n")        
        archivo.write("}\n")
        num+=1
archivo.close()
