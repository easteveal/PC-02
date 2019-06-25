#La historia de usuario se usa para hacer cualquier tipo de plan, y asi poder saber que es lo que se desea, para que , y en que lo puedo utilizar
#Como entrenador de futbol quiero saber la cantidad que gastare en articulos deportivos para llevar un control en gastos mensuales

a=int(input("Ingrese la cantidad de camisetas que va a comprar:"))
b=int(input("Ingrese la cantidad de shorts que va a comprar:"))
c=int(input("Ingrese la cantidad de medias que va a comprar:"))
d=int(input("Ingrese la cantidad de guantes que va a comprar:"))
e=int(input("Ingrese la cantidad de pelotas que va a comprar:"))

#Cantidad en soles
camisetas = 5
pelotas = 15
shorts = 3
medias = 1
guantes = 10
suma=0
mensaje=""
if a>0:
    resultado = camisetas*a
else:
    mensaje= "Incorrecto"
    print(mensaje)
if b>0:
    resultado1 = shorts*b
else:
    mensaje= "Incorrecto"
    print(mensaje)
if c>0:
    resultado2 = medias*c
else:
    mensaje= "Incorrecto"
    print(mensaje)
if d>0:
    resultado3 = guantes*d
else:
    mensaje= "Incorrecto"
    print(mensaje)
if e>0:
    resultado4 = pelotas*e
else:
    mensaje= "Incorrecto"
    print(mensaje)

suma = resultado+resultado1+resultado2+resultado3+resultado4

print ("Usted gastara", suma , "soles" )
