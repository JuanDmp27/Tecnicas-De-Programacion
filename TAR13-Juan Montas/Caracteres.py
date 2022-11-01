#Módulos (Juan Daniel Montas Peralta. jm21-1819)
#Diccionario de caracteres

def Primero(Opcion): 
    def Caracteres(Caracter):
    
        #creamos un for para contar los caracteres
    
        for x in Caracter :
        
            Numeros= Caracter.count(x)
            #Creamos un diccionario para almacenar los caracteres
            Diccionario= {
            x : Numeros
            }
    
        
    
            #Por ultimo imprimimos el diccionario
            print(Diccionario)
    
    #Hacemos que el usuario llame a la funcion
    Caracter = input('Diga su palabra: ')
    Caracteres(Caracter)