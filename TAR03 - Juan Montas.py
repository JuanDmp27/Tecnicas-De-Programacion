from ast import If

#Aqui le proporciono la informacion al usuario para que pueda usar el programa
print("Saludos querido usuario Favor de colocar el tipo")
print("R= Residencial")
print("C= Comercio")
print("I= Industria")
print("Las letras deben estar en Mayusculas")

#Aqui ingresa el Tipo y lo que Comsume

Consumo = int(input("ingrese el Consumo"))
Tipo = input("Dime tu Tipo [R o C o I]: ")

#Aqui se comienza con las operaciones de if

if Tipo == "R" or Tipo == "C" or Tipo == "I":
	print("Procesajdo")

#En el caso de que elija R (Residencial)
if Consumo > 500 and Tipo == 'R' :
    print("Usted paga RD$850.00")
elif Consumo < 500 and Tipo == 'R' :
    print("Usted paga RD$550.00")

#En el caso de que elija C (Comercio)
elif Consumo > 1000 and Tipo == 'C' :
    print("Usted paga RD$2500.00")
elif Consumo < 1000 and Tipo == 'C' :
    print("Usted paga RD$1300.00")
     
#En el caso de que elija I (industria)
elif Consumo > 5000 and Tipo == 'I' :
    print("Usted paga RD$4200.00")
elif Consumo < 5000 and Tipo == 'I' :
    print("Usted paga 	RD$3800.00")

#En el caso de que elija otra opcion.

else:
    print("Coloque las opciones pedidas")


#Juan Daniel Montas P 
#jm21-1819











 

