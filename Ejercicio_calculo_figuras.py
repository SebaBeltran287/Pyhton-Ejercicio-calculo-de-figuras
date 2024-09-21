import math #importo libreria de funciones
import os
os.system("cls") #comando para limpiar la pantalla

#le doy valor a lo que debo calcular
perimetro=0     
area=0
hipotenusa=0
lado=0
lado1=0
lado2=0
radio=0
altura=0
base=0

#le doy a seleccionar una figura "cuadrado, circulo y triangulo" (1,2,3)
print("ESCOGA UNA FIGURA:")
print("1. Cuadrado")
print("2. Circulo")
print("3. Triángulo")
opcion=(input("Seleccione una alternativa (1/2/3): ")) #espero y almaceno la desicion en "opcion"

#le doy a seleccionar opciones "Area o Perimetro (a/b)"
print("¿Que desea calcular?")
print("a. Area")
print("b. Perimetro" )
tipodecalculo=input("Seleccione una alternativa (a/b): ") #espero y almaceno la desicion en "tipodecalculo"

if opcion=="1": #si escoge cuadrado se ejecuta
    if tipodecalculo=="a": #si escoge calcular area (a)
        lado=float(input("Ingrese un lado del cuadrado: ")) #pregunto por un lado del cuadrado
        area=round(lado*lado, 2)
        print(f"El area del cuadrado es {area}")
    elif tipodecalculo=="b": #si escoge calcular perimetro
        lado=float(input("Ingrese un lado del cuadrado: ")) #pregunto por un lado del cuadrado
        perimetro=round(4*lado, 2)
        print(f"EL perimetro del cuadrado es {perimetro}")
    else: #si no seleciona una opcion valida ni area ni perimetro (a/b)
        print("Error") 
        print("No seleccionó ninguna opción válida")
elif opcion=="2": #si escoge circulo se ejecuta
    if tipodecalculo=="a": #si escoge calcular area (a)
        radio=float(input("Ingrese el radio del circulo: ")) #pregunto por el radio del circulo
        area=math.pi*math.pow(radio,2)
        area=round(area, 2)
        print(f"El area del circulo es {area}")
    elif tipodecalculo=="b": #si escoge calcular perimetro
        radio=float(input("Ingrese el radio del circulo: ")) #pregunto por la base del circulo
        perimetro=round(2*math.pi*radio, 2)
        print(f"EL perimetro del circulo es {perimetro}")
    else: #si no seleciona una opcion valida  ni area ni perimetro (a/b)
        print("Error")
        print("No seleccionó ninguna opcicón válida") 
elif opcion=="3": #si escoge triangulo se ejecuta
    if tipodecalculo=="a": #si escoge calcular area (a)
        altura=float(input("Ingrese la altura del triangulo: ")) #pregunto por la altura del triangulo
        base=float(input("Ingrse la base del triangulo: ")) #pregunto por la base del triangulo
        area=(altura*base)/2
        area=round(area, 2)
        print(f"El area del triangulo es {area}")
    elif tipodecalculo=="b": #si escoge calcular perimetro
        lado1=float(input("Ingrese un cateto del triangulo: ")) #pregunto por un cateto
        lado2=float(input("Ingrese el otro cateto del triangulo: ")) #pregunto por el otro cateto
        hipotenusa=math.pow(lado1,2)+math.pow(lado2,2)
        hipotenusa=math.sqrt(hipotenusa)
        perimetro=round(lado1+lado2+hipotenusa, 2)
        hipotenusa=round(hipotenusa, 2)
        print(f"EL perimetro del triangulo es {perimetro}") 
        respuesta=input("Tambien desea calcular la hipotenusa(si/no): ") #espero y almaceno su respuesta
        if respuesta=="si": #si desea calcular la hipotenusa, se ejecuta
            print(f"La hipotenusa mide {hipotenusa}") 
        elif respuesta=="no": #si no desea calcular la hipotenusa
            print("Fin")
        else:
            print("Error")
            print("No seleccionó ninguna opción válida")
    else: #si no seleciona una opcion valida ni area ni perimetro (a/b)
        print("Error")
        print("No seleccionó ninguna opción válida")  
else: #si no seleciona una opcion valida si no se selecciona cuadrado ni circulo ni triangulo(1,2,3)
    print("Error")
    print("No seleccionó ninguna opción válida") 

