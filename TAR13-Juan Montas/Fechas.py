#Solicitar una fecha por teclado
def Activador(Opcion) :
    #Importamos datetime
    import datetime

    #Hacemos que el ususario elija la fecha
    Dia= int(input('introduzca dia: '))
    Mes = int(input("Introduzca mes: "))
    Año = int(input("Introduzca Año: "))

    Fecha = datetime.date(Año, Mes, Dia)

    #Mediante condiconales determinamos los dias de semana
    if Fecha.weekday() == 0 :
        print("lunes %s"%(Fecha.strftime("%d, %b, %Y")))
    elif Fecha.weekday() == 1 :
        print("martes %s"%(Fecha.strftime("%d, %b, %Y")))
    elif Fecha.weekday() == 2 :
        print("miercoles %s"%(Fecha.strftime("%d, %b, %Y")))
    elif Fecha.weekday() == 3 :
        print("jueves %s"%(Fecha.strftime("%d, %b, %Y")))
    elif Fecha.weekday() == 4 :
        print("viernes %s"%(Fecha.strftime("%d, %b, %Y")))
    elif Fecha.weekday() == 5 :
        print("Sabado %s"%(Fecha.strftime("%d, %b, %Y")))
    elif Fecha.weekday() == 6 :
        print("Domingo %s"%(Fecha.strftime("%d, %b, %Y")))



