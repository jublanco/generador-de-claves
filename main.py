#Generador de claves
#Primero importamos el modulo secret con su funcion choice
from secrets import choice
#Importamos todos los caracteres del modulo string
from string import ascii_letters, ascii_uppercase, digits

#En una variable le decimos cuales son los caracteres que tiene que elegir
caracteres = ascii_letters + ascii_uppercase + digits
#Con otra variable le decimos la longitud del mismo
longitud = int(input("Escriba la longitud de su clave: "))
#Con la funcion join le decimos que eleja con choice un caracter y haga lo mismo 8 veces
Contraseña = ''.join(choice(caracteres) for caracter in range(longitud))
print('Su clave es: ', Contraseña)