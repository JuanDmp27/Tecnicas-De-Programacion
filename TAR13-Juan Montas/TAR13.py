import Caracteres
import Fechas
from Fechas import Activador
from Caracteres import Primero




print("Escribir 1 si desea los caracteres")
print("Escribir 2 si desea las fechas")
Opcion = int(input("diga su opcion: "))

if  Opcion == 1 :
    print("comenzando el programa")
    Caracteres.Primero(Opcion)
    print("Finalizando el programa")
elif Opcion == 2 :
    print("comenzando el programa")
    Fechas.Activador(Opcion)
    print("Finalizando el programa")

else:
    print("no se encuentra esa opcion")
